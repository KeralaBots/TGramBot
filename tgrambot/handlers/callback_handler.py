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

import tgrambot
from typing import Callable

from .handler import Handler


class CallbackQueryHandler(Handler):
    def __init__(self, callback: Callable, filters=None):
        super(CallbackQueryHandler, self).__init__(callback, filters)
        self.required_filters = ['callback_data', 'regex']

    async def check(self, bot: 'tgrambot.Bot', update):
        if self.filters:
            filter_type = self.filters.get('type')
            if filter_type and filter_type in self.required_filters and update.callback_query:
                if filter_type == "callback_data":
                    if update.callback_query.data:
                        data = self.filters.get('data')
                        m = re.search(data, update.callback_query.data, re.I)
                        if m:
                            return True
                        else:
                            return False
                    else:
                        return False
                elif filter_type == "regex":
                    regex = self.filters.get('regex')
                    if update.callback_query.data:
                        m = re.search(regex, update.callback_query.data, re.I)
                        if m:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return True
