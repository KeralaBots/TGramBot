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

from typing import Union


class Filters:
    def __init__(self):
        self.type = 'all'

    document = dict(type="document")

    audio = dict(type="audio")

    video = dict(type="video")

    video_note = dict(type="video_note")

    voice = dict(type="voice")

    sticker = dict(type="sticker")

    animation = dict(type="animation")

    via_bot = dict(type="via_bot")

    poll = dict(type="poll")

    caption = dict(type="caption")

    dice = dict(type="dice")

    game = dict(type="game")

    venue = dict(type="venue")

    location = dict(type="location")

    new_chat_title = dict(type="new_chat_title")

    new_chat_photo = dict(type="new_chat_photo")

    invoice = dict(type="invoice")

    video_chat_scheduled = dict(type="video_chat_scheduled")

    video_chat_started = dict(type="video_chat_started")

    video_chat_ended = dict(type="video_chat_ended")

    video_chat_participants_invited = dict(type="video_chat_participants_invited")

    successful_payment = dict(type="successful_payment")

    all = dict(type="all")

    @staticmethod
    def command(commands: Union[str, list], prefixes: Union[list, str] = "/"):
        handler_dict = dict(
            type="command",
            command=commands,
            prefix=prefixes
        )
        return handler_dict

    @staticmethod
    def text(text: str = None):
        handler_dict = dict(
            type="text",
            text=text
        )
        return handler_dict

    @staticmethod
    def regex(regex: str):
        handler_dict = dict(
            type="regex",
            regex=regex
        )
        return handler_dict

    @staticmethod
    def callback_data(data: str):
        handler_dict = dict(
            type="callback_data",
            data=data
        )
        return handler_dict

    private = dict(type="chat", chat_type="private")

    group = dict(type="chat", chat_type="group")

    supergroup = dict(type="chat", chat_type="supergroup")

    channel = dict(type="chat", chat_type="channel")
