from TelegramBOT.login import bot

height, weight = 0, 0


def input_height(message):
    msg = bot.reply_to(message, 'Напиши рост')
    bot.register_next_step_handler(msg, find_height)


def input_weight(message):
    msg = bot.reply_to(message, 'Напиши вес')
    bot.register_next_step_handler(msg, find_weight)


def find_height(message):
    print(message.text)
    message.text = (message.text).replace(',', '.')
    try:
        message.text = float(message.text)
        if message.text > 0:
            global height
            height = message.text
            input_weight(message)
            print(height)
        else:
            print(message.text)
            bot.send_message(message.chat.id, 'Рост не может быть <=0, давай ещё раз!')
            input_height(message)
    except:
        print(message.text)
        bot.send_message(message.chat.id, 'Что ты написал вообще?')
        input_height(message)


def find_weight(message):

    print(message.text)
    message.text = (message.text).replace(',', '.')
    try:
        message.text = float(message.text)
        if message.text > 0:
            global weight
            weight = message.text
            imt_calculation(message)
            print(weight)
        else:
            print(message.text)
            bot.send_message(message.chat.id, 'Вес не может быть <=0, давай ещё раз!')
            input_weight(message)
    except:
        print(message.text)
        bot.send_message(message.chat.id, 'Может ты не так меня понял?')
        input_weight(message)


def imt_calculation(message):
    imt_result = round((weight / (height / 100) ** 2), 2)
    weight_interpreter = ''
    if imt_result > 40:
        weight_interpreter = ': ожирение 3-й степени'
    if 35 <= imt_result < 40:
        weight_interpreter = ': ожирение 2-й степени'
    if 30 <= imt_result < 35:
        weight_interpreter = ': ожирение 1-й степени'
    if 25 <= imt_result < 30:
        weight_interpreter = ': предожирение (избыточная масса)'
    if 18.5 <= imt_result < 25:
        weight_interpreter = ': нормальный вес (оптимальный)'
    if 16 <= imt_result < 18.5:
        weight_interpreter = ': недостаточный вес'
    if imt_result < 16:
        weight_interpreter = ': анорексия (дефицит веса)'
    weight_recommended = round(21.75 * (height / 100) ** 2, 2)
    bot.send_message(message.chat.id, str(imt_result) + weight_interpreter + "\n" +
                     'Рекомендуемый вес для данного роста ' + str(weight_recommended))
    bot.send_message(message.chat.id, '/start')
