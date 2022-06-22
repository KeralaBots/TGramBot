# TGramBot - Partially Auto-generated Telegram Bot Api Library Python
# Copyright (C) 2022  Anand <anandpskerala@gmail.com>

# TGramBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# TGramBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import inspect
import logging
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor

import tgrambot

import signal
from signal import signal as signal_fn, SIGINT, SIGTERM, SIGABRT


log = logging.getLogger(__name__)

# Signal number to name
signals = {
    k: v for v, k in signal.__dict__.items()
    if v.startswith("SIG") and not v.startswith("SIG_")
}


class Dispatcher:
    def __init__(self, bot: "tgrambot.Bot", workers: int):
        self.bot = bot
        self.loop = asyncio.get_event_loop_policy().get_event_loop()
        self.workers = workers
        self.groups = OrderedDict()
        self.executor = ThreadPoolExecutor(workers, thread_name_prefix="Handler")
        self.is_idling = False
        self.is_running = False

    async def start(self):
        self.is_running = True
        asyncio.ensure_future(self.handle_workers())

    async def handle_workers(self):
        while self.is_running:
            updates = await self.bot.get_updates(offset=self.bot.offset + 1)
            for update in updates:
                if update is None:
                    break
                self.bot.offset = update.update_id
                try:
                    update = update

                    for group in self.groups.values():
                        for handler in group:
                            check = await handler.check(self.bot, update)
                            updated = self._parse_updates(update)
                            if check:
                                if inspect.iscoroutinefunction(handler.callback):
                                    await handler.callback(self.bot, updated)
                                else:
                                    self.loop.run_in_executor(
                                        self.executor,
                                        handler.callback,
                                        self.bot,
                                        updated
                                    )
                                break
                except Exception as exe:
                    logging.error(exe, exc_info=True)

    async def idle(self):

        def signal_handler(signum, __):
            log.info(f"Stop signal received ({signals[signum]}). Exiting...")
            self.is_idling = False

        for s in (SIGINT, SIGTERM, SIGABRT):
            signal_fn(s, signal_handler)

        self.is_idling = True
        log.info('[Bot] Started Bot session. Idling....')

        while self.is_idling:
            await asyncio.sleep(1)

    async def stop(self):
        self.is_running = False
        self.groups.clear()

    def add_handler(self, handler, group: int):
        try:
            if group not in self.groups:
                self.groups[group] = []
                self.groups = OrderedDict(sorted(self.groups.items()))

            self.groups[group].append(handler)
        finally:
            pass

    @staticmethod
    def _parse_updates(update):
        if update.inline_query:
            updated = update.inline_query
        elif update.callback_query:
            updated = update.callback_query
        elif (update.message or update.edited_message or update.channel_post
        or update.edited_channel_post):
            updated = update.message
        else:
            updated = update

        return updated
