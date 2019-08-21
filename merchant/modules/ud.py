import requests
from pyrogram import Filters, Message

from merchant import BOT
from merchant.helpers import ReplyCheck


def define_word_ud(word):
    def get_data(word_):
        r = requests.get(
            "http://api.urbandictionary.com/v0/define?term={}".format(word_)
        )
        if r.status_code == 200:
            data_ = r.json()
            return data_

    def get_definitions(data_):
        definitions_ = []
        for definition in data_["list"]:
            definitions_.append(
                "{}\t{}\t{}".format(
                    definition["word"], definition["definition"], definition["example"]
                )
            )
        return definitions

    def get_results(deft):
        definitions_ = ""
        for i in range(3):
            definition = definitions_[i].split("\t")
            word_ = deft[0]
            definition_ = deft[1]
            example = deft[2]
            definitions_ = "{}\n**{}**\n{}\n\nExample:\n{}\n\n".format(
                definition, word_, definition_, example
            )
        return definitions_

    data = get_data(word)
    definitions = get_definitions(data)
    definitions__ = get_results(definitions)
    return definitions__


@BOT.on_message(Filters.command("ud", "/") & ~Filters.edited)
async def post_ud(bot: BOT, message: Message):
    topic = ' '.join(message.command[1:])
    text = define_word_ud(topic)
    await BOT.send_message(
        chat_id=message.chat.id,
        text=text[:4096],
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )
    if text[4096:]:
        await BOT.send_message(
            chat_id=message.chat.id,
            text=text[4096:],
            disable_notification=True
        )
    if message.from_user.is_self:
        message.delete()
