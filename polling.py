from time import sleep

from conf import bot

from threading import Thread


def bot_polling():
    while True:
        try:
            print("Bot has been started successfully!")
            bot.polling(none_stop=True, interval=3, timeout=30)
        except Exception:
            bot.stop_polling()
            sleep(30)
        else:
            bot.stop_polling()
            break

    polling_thread = Thread(target=bot_polling)
    polling_thread.daemon = True
    polling_thread.start()

    if __name__ == "__main__":
        while True:
            try:
                sleep(120)
            except KeyboardInterrupt:
                break
