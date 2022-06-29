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
import re
import json

import tgrambot
from typing import Callable

from .handler import Handler


class MessageHandler(Handler):
    def __init__(self, callback: Callable, filters=None):
        super(MessageHandler, self).__init__(callback, filters)
        self.exclude = ['callback_data']
        self.special_types = ['command', 'all', 'regex', 'text', 'chat']

    async def check(self, bot: 'tgrambot.Bot', update):
        if self.filters:
            filter_type = self.filters.get('type')
            update_json = json.loads(update.message.json())
            if filter_type and update.message:
                if filter_type not in self.special_types and filter_type not in self.exclude:
                    if update_json.get(filter_type):
                        return True
                    else:
                        return False
                elif filter_type in self.special_types:
                    if filter_type == "command":
                        prefixes = self.filters.get('prefix')
                        commands = self.filters.get('command')
                        if update.message.text:
                            if type(prefixes) is str:
                                if update.message.text.startswith(prefixes):
                                    pass
                                else:
                                    return False
                            else:
                                for pre in prefixes:
                                    if update.message.text.startswith(pre):
                                        pass
                                    else:
                                        return False

                            if type(commands) is str:
                                m = re.search(commands, update.message.text, re.I)
                                if m:
                                    return True
                                else:
                                    return False
                            else:
                                for command in commands:
                                    m = re.search(command, update.message.text, re.I)
                                    if m:
                                        return True
                                    else:
                                        return False
                    elif filter_type == 'regex':
                        regex = self.filters.get('regex')
                        if update.message.text:
                            m = re.search(regex, update.message.text, re.I)
                            if m:
                                return True
                            else:
                                return False
                    elif filter_type == 'text':
                        text = self.filters.get('text')
                        if update.message.text:
                            if text:
                                m = re.search(text, update.message.text, re.I)
                                if m:
                                    return True
                                else:
                                    return False
                            else:
                                return True
                    elif filter_type == 'chat':
                        chat_type = self.filters.get('chat_type')
                        if update.message and update.message.chat.type == chat_type:
                            return True
                        else:
                            return False
                else:
                    if update.message:
                        return True
                    else:
                        return False
        else:
            if update.message:
                return True
            else:
                return False
