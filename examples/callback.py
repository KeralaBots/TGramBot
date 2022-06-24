from tgrambot import Bot
from tgrambot.types import CallbackQuery

bot = Bot(
    token="",
    workers=50,
    parse_mode="Markdown"
)


@bot.on_callback()
async def callback_echo(c: Bot, m: CallbackQuery):
    await c.answer_callback_query(m.id, "Echo", show_alert=True)