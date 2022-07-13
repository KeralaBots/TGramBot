import os
import json
import tgrambot

from .errors import InstanceNotFound


def create_instance(bot: "tgrambot.Bot"):
    if os.path.exists('tgrambot.session'):
        os.remove('tgrambot.session')

    instance = open('tgrambot.session', mode='w')
    data = json.dumps({
        'token': bot.bot_token,
        'parse_mode': bot.parse_mode,
        'proxy': bot.proxy
    })
    instance.write(data)


def delete_instance():
    if os.path.exists('tgrambot.session'):
        os.remove('tgrambot.session')


def get_current_instance() -> "tgrambot.Bot":
    try:
        with open('tgrambot.session', mode='r') as f:
            data = json.loads(f.read())
            bot = tgrambot.Bot(
                token=data.get('token'),
                parse_mode=data.get('parse_mode'),
                proxy_url=data.get('proxy')
            )
            return bot
    except FileNotFoundError:
        raise InstanceNotFound
