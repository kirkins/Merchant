import requests
import asyncio

from random import randint
import re

from pyrogram import Filters, Message

from merchant import BOT
from merchant.helpers import ReplyCheck


def get_video():
    seed = str(randint(0, 100000000))
    url = "https://hooktube.com/random?" + seed
    r = requests.get(url)
    return r.url.replace("hooktube", "youtube", 1)


@BOT.on_message(Filters.regex("(?i)(post|get|send) (random) (youtube|hooktube|video)"))
async def send_dog(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (random) (youtube|hooktube|video)", message.text):
        text = get_video()
        await BOT.send_message(
            chat_id=message.chat.id,
            text=text,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
