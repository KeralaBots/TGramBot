# TGramBot

TGramBot is a partially auto-generated and asynchronous Minimal [Telegram Bot API](https://core.telegram.org/bots/api) framework in Python for bots

This library is inspired by a number of other libraries:

- [Gotgbot](https://github.com/PaulSonOfLars/gotgbot), [telegram-bot-api-spec](https://github.com/PaulSonOfLars/telegram-bot-api-spec) by [Paul Larsen
](https://github.com/PaulSonOfLars)
- [aiogram](https://github.com/aiogram/aiogram)

Special thanks to [Paul Larsen
](https://github.com/PaulSonOfLars) for his libraries

__**This Library is still in its Alpha phase**__

So the chance of getting bugs and errors are high. So please let us know through the [issue section](https://github.com/KeralaBots/TGramBot/issues) about the bug you have encountered.


### Installing..

```
pip3 install tgrambot
```

### Example

```python
import asyncio

from tgrambot import Bot
from tgrambot.filters import Filters
from tgrambot.types import Message


bot = Bot("token", **kwargs)

@bot.on_message(Filters.command('start'))
async def start_bot(c: Bot, m: Message):
    await c.send_message(m.chat.id, "Hola Amigo!")

async def main():
    await bot.run()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

### More Examples will be published soon
