from conf import bot
from polling import bot_polling

from transliterate import (
    to_latin,
    to_cyrillic
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.first_name
    wel_txt = f"Hello and Welcome <b>{username}</b> 🎉\n"
    wel_txt += "Send to me any messages for to see proccess \nExample: Telegram -> Телеграм 🔺🔻"
    bot.send_message(message.chat.id, wel_txt, parse_mode="HTML")


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    def javob(msg): return to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot_polling()