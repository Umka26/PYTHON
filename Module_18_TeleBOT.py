import telebot
from Module_18_TOKEN import TOKEN
from Module_18_extensions import ConvertionException, CryptoConverter, keys


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, "Красивое фото, но мое предназначение в другом!\nЯ перевожу валюту!\nДля начала работы введите команду /start или /help")

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду в следующем формате:\n<имя валюты> \
<в какую валюту хотите перевести> \
<количество переводимой валюты>\nЧтобы увидеть список доступных валют введите команду /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def handle_start_values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    try:
        if len(values) != 3:
            raise ConvertionException('Вы ввели неверные параметры!\nПример ввода данных:\nдоллар евро 10')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена "{amount}" "{quote}" в "{base}" - "{total_base}"'
        bot.send_message(message.chat.id, text)


bot.polling()