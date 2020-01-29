import pyowm
import requests
import telebot

token_bot = "***"
BASE_URL = 'https://api.telegram.org/bot<token>/'
token_owm = '***'


bot = telebot.TeleBot(token_bot)
owm = pyowm.OWM(token_owm, language='ru')
r = requests.get(f'{BASE_URL}getMe')
