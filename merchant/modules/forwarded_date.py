from datetime import datetime

from pyrogram import Filters, Message

from merchant import BOT


def get_month(message):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    int_month = int(datetime.utcfromtimestamp(message.reply_to_message.forward_date).strftime('%m'))
    return switcher.get(int_month)


@BOT.on_message(Filters.reply & Filters.command(commands=['sentdate', 'sentdate@videomerchantbot'], prefixes='/'))
async def get_forwarded_message_date(bot: BOT, message: Message):
    year = datetime.utcfromtimestamp(message.reply_to_message.forward_date).strftime('%Y')
    month = get_month(message)
    day = datetime.utcfromtimestamp(message.reply_to_message.forward_date).strftime('%d')
    time = datetime.utcfromtimestamp(message.reply_to_message.forward_date).strftime('%H:%M:%S')
    original_date = '{}. {} {} at {}'.format(day, month, year, time)

    await BOT.send_message(
        chat_id=message.chat.id,
        text='This message was sent on {} GMT'.format(original_date),
        reply_to_message_id=message.reply_to_message.message_id
    )
