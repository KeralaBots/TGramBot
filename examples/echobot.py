import asyncio

from tgrambot import Bot
from tgrambot.types import Message

bot = Bot(
    token="",
    workers=50,
    parse_mode="Markdown"
)


@bot.on_message()
async def echo(c: Bot, m: Message):
    await c.send_message(m.chat.id, m.text)


async def main():
    await bot.start()
    await bot.idle()
    await bot.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
