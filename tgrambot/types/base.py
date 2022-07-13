# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#       This is an auto-generated file!       #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


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

import logging
from pydantic import BaseModel
from typing import List, Union

import tgrambot
from ..storage import get_current_instance
from ..errors import MethodNotFound

logger = logging.getLogger(__name__)


class TelegramObject(BaseModel):

    """
    Base TelegramObject Class for TGramBot
    """

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return f"<{type(self).__name__} {self}>"

    async def reply_text(self, text: str, parse_mode: str = None, entities: "List[tgrambot.types.MessageEntity]" = None, disable_web_page_preview: bool = None, disable_notification: bool = None, protect_content: bool = None, allow_sending_without_reply: bool = None, reply_markup: "Union[tgrambot.types.InlineKeyboardMarkup, tgrambot.types.ReplyKeyboardMarkup, tgrambot.types.ReplyKeyboardRemove, tgrambot.types.ForceReply]" = None):
        if isinstance(self, tgrambot.types.Message):
            bot = get_current_instance()
            await bot.send_message(
                chat_id=self.chat.id,
                text=text,
                parse_mode=parse_mode or bot.parse_mode,
                entities=entities,
                reply_to_message_id=self.message_id,
                disable_notification=disable_notification,
                disable_web_page_preview=disable_web_page_preview,
                protect_content=protect_content,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup
            )
        else:
            raise MethodNotFound('reply_text', type(self).__name__)

    async def answer(self, text: str = None, show_alert: bool = None, url: str = None, cache_time: int = None):
        if isinstance(self, tgrambot.types.CallbackQuery):
            bot = get_current_instance()
            return await bot.answer_callback_query(
                callback_query_id=self.id,
                text=text,
                show_alert=show_alert,
                url=url,
                cache_time=cache_time
            )
        else:
            raise MethodNotFound('answer', type(self).__name__)

    async def forward(self, chat_id: Union[int, str], disable_notification: bool = None, protect_content: bool = None):
        if isinstance(self, tgrambot.types.Message):
            bot = get_current_instance()
            message = await bot.forward_message(
                chat_id=chat_id,
                from_chat_id=self.chat.id,
                message_id=self.message_id,
                disable_notification=disable_notification,
                protect_content=protect_content
            )

            return message
        else:
            raise MethodNotFound('forward', type(self).__name__)

    async def copy_message(self, chat_id: Union[int, str], caption: str = None, parse_mode: str = None, caption_entities: "List[tgrambot.types.MessageEntity]" = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: "Union[tgrambot.types.InlineKeyboardMarkup, tgrambot.types.ReplyKeyboardMarkup, tgrambot.types.ReplyKeyboardRemove, tgrambot.types.ForceReply]" = None):
        if isinstance(self, tgrambot.types.Message):
            bot = get_current_instance()
            message_id = await bot.copy_message(
                chat_id=chat_id,
                from_chat_id=self.chat.id,
                message_id=self.message_id,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup
            )
            return message_id
        else:
            raise MethodNotFound('copy_message', type(self).__name__)

    async def reply_photo(
            self,
            photo: "Union[tgrambot.types.InputFile, str]",
            caption: str = None,
            parse_mode: str = None,
            caption_entities: "List[tgrambot.types.MessageEntity]" = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            allow_sending_without_reply: bool = None,
            reply_markup: "Union[tgrambot.types.InlineKeyboardMarkup, tgrambot.types.ReplyKeyboardMarkup, tgrambot.types.ReplyKeyboardRemove, tgrambot.types.ForceReply]" = None
    ):
        if isinstance(self, tgrambot.types.Message):
            bot = get_current_instance()
            return await bot.send_photo(
                self.chat.id,
                photo=photo,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                disable_notification=disable_notification,
                protect_content=protect_content,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup
            )
        else:
            raise MethodNotFound('reply_photo', type(self).__name__)

    async def ban(self, user_id: int, until_date: int = None, revoke_messages: bool = None):
        if isinstance(self, tgrambot.types.Chat):
            bot = get_current_instance()
            return await bot.ban_chat_member(
                chat_id=self.id,
                user_id=user_id,
                until_date=until_date,
                revoke_messages=revoke_messages
            )
        else:
            raise MethodNotFound('ban', type(self).__name__)

    async def unban(self, user_id: int, only_if_banned: bool = None):
        if isinstance(self, tgrambot.types.Chat):
            bot = get_current_instance()
            return await bot.unban_chat_member(
                chat_id=self.id,
                user_id=user_id,
                only_if_banned=only_if_banned
            )
        else:
            raise MethodNotFound('unban', type(self).__name__)

    async def pin(self, disable_notification: bool = None):
        if isinstance(self, tgrambot.types.Message):
            bot = get_current_instance()
            return await bot.pin_chat_message(
                chat_id=self.chat.id,
                message_id=self.message_id,
                disable_notification=disable_notification
            )
        else:
            raise MethodNotFound('pin', type(self).__name__)

    async def unpin(self):
        if isinstance(self, tgrambot.types.Message):
            bot = get_current_instance()
            return await bot.unpin_chat_message(
                chat_id=self.chat.id,
                message_id=self.message_id
            )
        else:
            raise MethodNotFound('unpin', type(self).__name__)
