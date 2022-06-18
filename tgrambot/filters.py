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
