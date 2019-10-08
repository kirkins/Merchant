import asyncio

from pyrogram import Filters, Message
from merchant import BOT, LOGS

from PyDictionary import PyDictionary

dictionary = PyDictionary()


def get_definition(key_word):
    results_dict = dictionary.meaning(key_word)
    defined = ""

    for key in results_dict:
        definitions = "\n**{}**".format(key)
        for definition in results_dict[key]:
            definitions = definitions + "\n{}".format(definition)

        defined = "{}\n{}".format(defined, definitions)

    return defined


@BOT.on_message(Filters.text & ~Filters.edited & Filters.command(commands = 'define', prefixes='/'))
async def translate_word(bot: BOT, message: Message):
    commands_length = len(message.command)
    word = message.command[1]
    definition = get_definition(word)

    if commands_length == 2:
        await message.reply("{}".format(definition))
    else:
        await message.reply("Define a single word\n\nExample: /define car")     
