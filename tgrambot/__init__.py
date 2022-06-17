import re
from .bot import Bot

with open('tgrambot/version.txt', encoding='utf-8') as f:
    __version__ = re.findall(r'__version__ = \"(.+)\"', f.read())[0]

__all__ = ["Bot"]
