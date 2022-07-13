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
from ..types import InlineQuery


class InlineQueryHandler(Handler):
    def __init__(self, callback: Callable, filters=None):
        super(InlineQueryHandler, self).__init__(callback, filters)
        self.required_filters = ['regex']
    
    async def check(self, bot: 'tgrambot.Bot', update):
        if isinstance(update, InlineQuery):
            if self.filters:
                filter_type = self.filters.get('type')
                if filter_type and filter_type in self.required_filters:
                    if update.query:
                        regex = self.filters.get('regex')
                        m = re.search(regex, update.query, re.I)
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
        else:
            return False
