from environs import Env
from telebot import TeleBot

env = Env()
env.read_env()

bot = TeleBot(token=env.str("BOT_TOKEN"))
