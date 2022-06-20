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
    User,
    Update,
    Message,
    InputFile,
    MessageEntity,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    MessageId
)

from .errors import InvalidToken, TelegramError

API_TIMEOUT = 60
RETRY = 3


class Bot:
    def __init__(
            self,
            token: str,
            parse_mode: str = None,
            workers: int = 50
    ):
        self.bot_token = self._validate_bot_token(token)
        self._api_url = f"https://api.telegram.org/bot{self.bot_token}/"
        self._file_url = f"https://api.telegram.org/file/bot{self.bot_token}/"
        self._loop = asyncio.get_event_loop()
        self.logger = logging.getLogger("TgramBot")
        self.offset = -1
        self._parse_mode = parse_mode
        self._parse_modes = ["MarkdownV2", "HTML", "Markdown", None]
        self.dispatcher = Dispatcher(self, workers)
        self.workers = workers

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

    def _get_api_url(self, method):
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

    async def get_updates(
            self,
            offset: int = None,
            limit: int = None,
            timeout: int = None,
            allowed_updates: List[str] = None
    ):
        payload = self._generate_payload(**locals())
        method = 'getUpdates'
        url = self._get_api_url(method)
        resp = await self._aio_post(url, payload)
        result = [Update(**r) for r in resp]
        return result

    async def get_me(self):
        payload = self._generate_payload(**locals())
        method = 'getMe'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload)
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

    async def log_out(self):
        payload = self._generate_payload(**locals())
        method = 'logOut'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload)
        return result

    async def close(self):
        payload = self._generate_payload(**locals())
        method = 'close'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload)
        return result

    async def send_message(
            self,
            chat_id: Union[int, str],
            text: str,
            parse_mode: str = None,
            entities: List[MessageEntity] = None,
            disable_web_page_preview: bool = False,
            disable_notification: bool = False,
            protect_content: bool = False,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = True,
            reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None
    ):
        payload = self._generate_payload(**locals())
        method = 'sendMessage'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload)
        return Message(**result)

    async def forward_message(
            self,
            chat_id: Union[str, int],
            from_chat_id: Union[str, int],
            message_id: int,
            disable_notification: bool = False,
            protect_content: bool = False
    ):
        payload = self._generate_payload(**locals())
        method = 'forwardMessage'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload)
        return Message(**result)

    async def copy_message(
            self,
            chat_id: Union[str, int],
            from_chat_id: Union[str, int],
            message_id: int,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List[MessageEntity] = None,
            disable_notification: bool = False,
            protect_content: bool = False,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = True,
            reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None
    ):
        payload = self._generate_payload(**locals())
        method = 'copyMessage'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload)
        return MessageId(**result)

    async def send_photo(
            self,
            chat_id: Union[int, str],
            photo: Union[InputFile, str],
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List[MessageEntity] = None,
            disable_notification: bool = False,
            protect_content: bool = False,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = True,
            reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None
    ):
        payload = self._generate_payload(**locals())
        files = self._attach_file(payload, 'photo', photo)
        method = 'sendPhoto'
        url = self._get_api_url(method)
        result = await self._aio_post(url, payload, files)
        return Message(**result)

    @staticmethod
    def _generate_payload(**kwargs):
        return_value = {}
        for key, value in kwargs.items():
            if key not in ['self', 'cls'] and value is not None and not key.startswith('_'):
                if key == 'reply_markup':
                    value = value.json() if value is not None else value
                return_value.update({key: value})
        return return_value

    @staticmethod
    def _attach_file(payload, key, file):
        if file and os.path.isfile(file):
            files = {key: open(file, 'rb')}
            payload.pop(key)
        else:
            files = None
            payload[key] = file

        return files

    @staticmethod
    async def _aio_post(url, payload, files=None):
        async with httpx.AsyncClient(http2=True) as client:
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
