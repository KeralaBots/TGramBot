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

