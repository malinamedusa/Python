from telebot import types

from TelegramBOT.imt_button import input_height
from TelegramBOT.login import bot
from TelegramBOT.weather_button import find_place


@bot.message_handler(commands=['start', 'help'])
def tap_button(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Узнать погоду', 'Рассчитать ИМТ')
    bot.reply_to(message, 'Я могу показать тебе погоду или посчитать ИМТ - тапай кнопку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def find_wish(message):
    if message.text == 'Узнать погоду':
        find_place(message)
    if message.text == 'Рассчитать ИМТ':
        input_height(message)


bot.polling(none_stop=True)
