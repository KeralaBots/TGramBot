import asyncio
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
        self.worker_tasks = []
        self.update_queue = asyncio.Queue()
        self.lock_lists = []
        self.groups = OrderedDict()
        self.executor = ThreadPoolExecutor(workers, thread_name_prefix="Handler")
        self.is_idling = False
        self.is_running = False

    async def start(self):
        self.is_running = True
        for i in range(self.workers):
            self.lock_lists.append(asyncio.Lock())

    @staticmethod
    def _parse_update(update):
        if (update.message or
                update.channel_post or
                update.edited_message or update.edited_channel_post
        ):
            updated = update.message
        else:
            updated = update

        return updated

    async def handle_workers(self, lock):
        while True:
            update = await self.update_queue.get()

            if update is None:
                break
            try:
                update = self._parse_update(update)

                async with lock:
                    for group in self.groups.values():
                        for handler in group:
                            pass
            except Exception as exe:
                self.bot.logger.log(exe, exc_info=True)

    async def idle(self):

        def signal_handler(signum, __):
            log.info(f"Stop signal received ({signals[signum]}). Exiting...")
            self.is_idling = False

        for s in (SIGINT, SIGTERM, SIGABRT):
            signal_fn(s, signal_handler)

        self.is_idling = True

        while self.is_idling:
            await asyncio.sleep(1)

    async def stop(self):
        self.is_running = False
        self.groups.clear()
        self.worker_tasks.clear()
        for i in range(self.workers):
            self.update_queue.put_nowait(None)
