import pyowm
import requests
import telebot

token_bot = "1031293192:AAGoYUaXkJOIWX1jB_U1e6gilchmGkbEJ8w"
BASE_URL = 'https://api.telegram.org/bot<token>/'
token_owm = 'd9d23e920d8ad8c8bb66d92bb7e9f0ac'


bot = telebot.TeleBot(token_bot)
owm = pyowm.OWM(token_owm, language='ru')
r = requests.get(f'{BASE_URL}getMe')
