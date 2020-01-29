from telebot import types

from TelegramBOT.login import owm, bot


def find_place(message):
    msg = bot.reply_to(message, 'Напиши город или страну')
    bot.register_next_step_handler(msg, find_weather)


def find_weather(message):
    try:
        observation = owm.weather_at_place(message.text)
        place = message.text
        w = observation.get_weather()
        temp_min = w.get_temperature('celsius')['temp_min']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        temp_max = w.get_temperature('celsius')['temp_max']
        humidity = w.get_humidity()  # 87
        wind = w.get_wind()['speed']  # {'speed': 4.6, 'deg': 330}
        answer = ('Погода в ' + place + "\n\n")
        answer += ('Тут сейчас ' + w.get_detailed_status() + "\n")
        if temp_min == temp_max:
            answer += ('Температура ' + str(temp_min) + ' градусов' + "\n")
        else:
            if min(temp_max, temp_min) < 0:
                answer += ('Температура от ' + str(temp_max) + ' до ' + str(temp_min) + ' градусов' + "\n")
            else:
                answer += ('Температура от ' + str(temp_min) + ' до ' + str(temp_max) + ' градусов' + "\n")
        answer += ('Влажность ' + str(humidity) + '%' + "\n")
        answer += ('Скорость ветра ' + str(wind) + 'м/c')
        bot.send_message(message.chat.id, answer)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Да', 'Нет')
        msg = bot.reply_to(message, 'Узнать погоду в другом городе?', reply_markup=markup)
        bot.register_next_step_handler(msg, reply_find_weather)
    except:
        answer: str = 'Неправильно ввел город. Давай ещё раз!'
        bot.send_message(message.chat.id, answer)
        find_place(message)


def reply_find_weather(message):
    print(message.text)
    print(message)
    if message.text == 'Да':
        msg = bot.reply_to(message, 'Напиши город или страну')
        bot.register_next_step_handler(msg, find_weather)
    else:
        bot.send_message(message.chat.id, '/start')
