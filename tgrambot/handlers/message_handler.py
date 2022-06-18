import asyncio
import re
import json

import tgrambot
from typing import Callable

from .handler import Handler


class MessageHandler(Handler):
    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
        self.exclude = ['callback_data']
        self.special_types = ['command', 'all', 'regex', 'text']

    async def check(self, bot: 'tgrambot.Bot', update):
        if self.filters:
            filter_type = self.filters.get('type')
            update_json = json.loads(update.json())
            if filter_type and update:
                if filter_type not in self.special_types and filter_type not in self.exclude:
                    if update_json.get(filter_type):
                        await self.callback[0](bot, update)
                        return True
                    else:
                        return False
                elif filter_type in self.special_types:
                    content = None
                    if filter_type == "command":
                        prefixes = self.filters.get('prefix')
                        commands = self.filters.get('command')
                        if update.text:
                            if type(prefixes) is str:
                                if update.text.startswith(prefixes):
                                    pass
                                else:
                                    return False
                            else:
                                for pre in prefixes:
                                    if update.text.startswith(pre):
                                        pass
                                    else:
                                        return False

                            if type(commands) is str:
                                m = re.search(commands, update.text, re.I)
                                if m:
                                    await self.callback[0](bot, update)
                                    return True
                                else:
                                    return False
                            else:
                                for command in commands:
                                    m = re.search(command, update.text, re.I)
                                    if m:
                                        await self.callback[0](bot, update)
                                        return True
                                    else:
                                        return False
                    elif filter_type == 'regex':
                        regex = self.filters.get('regex')
                        if update.text:
                            m = re.search(regex, update.text, re.I)
                            if m:
                                await self.callback[0](bot, update)
                                return True
                            else:
                                return False
                else:
                    if update:
                        await self.callback[0](bot, update)
                        return True
                    else:
                        return False
        else:
            await self.callback[0](bot, update)
            return True
