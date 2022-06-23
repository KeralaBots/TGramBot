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
import logging
import os
import json
import httpx
import contextvars
from typing import Optional, Union, List, Callable

from .dispatcher import Dispatcher
from .filters import Filters
from .handlers import MessageHandler, CallbackQueryHandler

from .types import (
    User
)

from .methods import Methods

from .errors import InvalidToken, TelegramError

API_TIMEOUT = 60
RETRY = 3


class Bot(Methods):
    def __init__(
            self,
            token: str,
            parse_mode: str = None,
            workers: int = 50,
            proxy_url: str = None,
            read_timeout: Optional[float] = 5.0,
            write_timeout: Optional[float] = 5.0,
            connect_timeout: Optional[float] = 5.0,
            pool_timeout: Optional[float] = 1.0,
    ):
        super(Bot, self).__init__(bot=self)
        self.bot_token = self._validate_bot_token(token)
        self._api_url = f"https://api.telegram.org/bot{self.bot_token}/"
        self._file_url = f"https://api.telegram.org/file/bot{self.bot_token}/"
        self._loop = asyncio.get_event_loop()
        self.logger = logging.getLogger(__name__)
        self.offset = -1
        self._parse_mode = parse_mode
        self._parse_modes = ["MarkdownV2", "HTML", "Markdown", None]
        self.dispatcher = Dispatcher(self, workers)
        self.workers = workers
        self.timeout = httpx.Timeout(
            connect=connect_timeout,
            read=read_timeout,
            write=write_timeout,
            pool=pool_timeout,
        )
        self.proxy = proxy_url

    @staticmethod
    def _validate_bot_token(token: str):
        token_str = token.split(":")
        if len(token_str) < 2:
            raise InvalidToken()

        if not token_str[0].isdigit():
            raise InvalidToken()
        return token

    @staticmethod
    def _extract_bot_id(token: str) -> int:
        raw_bot_id, *_ = token.split(":")
        return int(raw_bot_id)

    @property
    def id(self):
        return self._extract_bot_id(self.bot_token)

    def get_api_url(self, method):
        return f"{self._api_url.format(token=self.bot_token)}{method}"

    @property
    def parse_mode(self):
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, parse_mode: Optional[str] = None):
        if parse_mode not in self._parse_modes:
            raise ValueError('parse_mode must be one of {} or None. Not "{}"'.format(
                ", ".join(f'"{m}"' for m in self._parse_modes[:-1]),
                parse_mode
            ))
        self._parse_mode = parse_mode

    @parse_mode.deleter
    def parse_mode(self):
        self.parse_mode = None

    async def get_me(self):
        payload = self.generate_payload(**locals())
        method = 'getMe'
        url = self.get_api_url(method)
        result = await self.aio_post(url, payload)
        return User(**result)

    @property
    async def me(self):
        if not hasattr(self, '_me'):
            setattr(self, '_me', await self.get_me())
        return getattr(self, '_me')

    @me.deleter
    def me(self):
        if hasattr(self, '_me'):
            delattr(self, '_me')

    @staticmethod
    def generate_payload(**kwargs):
        return_value = {}
        for key, value in kwargs.items():
            if key not in ['self', 'cls'] and value is not None and not key.startswith('_'):
                if key == 'reply_markup':
                    value = value.json() if value is not None else value
                return_value.update({key: value})
        return return_value

    @staticmethod
    def attach_file(payload, key, file):
        if file and os.path.isfile(file):
            files = {key: open(file, 'rb')}
            payload.pop(key)
        else:
            files = None
            payload[key] = file

        return files

    async def aio_post(self, url, payload, files=None):
        async with httpx.AsyncClient(http2=True, timeout=self.timeout, proxies=self.proxy) as client:
            resp = await client.post(url, data=payload, files=files)
            try:
                data = resp.json()
            except json.JSONDecodeError:
                raise TelegramError('Error', resp.text)

            if not data['ok']:
                raise TelegramError(str(data['error_code']), str(data['description']))

            return data['result']

    async def start(self):
        self.logger.info("[Bot] Starting Bot session ...")
        await self.dispatcher.start()

    async def stop(self):
        self.logger.info("[Bot] Stopped Bot session ...")
        await self.dispatcher.stop()

    async def idle(self):
        await self.dispatcher.idle()

    async def run(self):
        await self.start()
        await self.idle()
        await self.stop()

    def on_message(self, filters: Filters = None, group: int = 0):
        def decorator(func):
            self.add_message_handler(func, filters, group)
        return decorator

    def on_callback(self, filters: Filters = None, group: int = 0):
        def decorator(func):
            self.add_callback_handler(func, filters, group)
        return decorator

    def add_message_handler(self, callback: Callable, filters: Filters = None, group: int = 0):
        handler = MessageHandler(callback, filters)
        self.dispatcher.add_handler(handler, group)

    def add_callback_handler(self, callback: Callable, filters: Filters = None, group: int = 0):
        handler = CallbackQueryHandler(callback, filters)
        self.dispatcher.add_handler(handler, group)
