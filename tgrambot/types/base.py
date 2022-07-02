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

logger = logging.getLogger(__name__)


class TelegramObject(BaseModel):

    """
    Base TelegramObject Class for TGramBot
    """

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return f"<{type(self).__name__} {self}>"
