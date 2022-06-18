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

from typing import Tuple


class TelegramError(Exception):
    def __init__(self, error: str, status: str):
        super().__init__()
        self.error = _parse_error(status, error)

    def __str__(self) -> str:
        return '%s' % self.error

    def __reduce__(self) -> Tuple[type, Tuple[str]]:
        return self.__class__, (self.error,)


def _parse_error(code: str, status: str):
    status = status.upper()
    parsed = f'[{status}] {code}'
    return parsed


class InvalidToken(TelegramError):
    def __init__(self):
        super().__init__('invalid token', "The given token is not valid")

    def __reduce__(self) -> Tuple[type, Tuple]:
        return self.__class__, ()

