import re

def regexFun(argText):
    import re   
    try:
        t = re.match(r'[0-9]{5,20}', argText)
        tt = t.group(0)
        tText = argText.replace(tt,'')
        return tt, tText

    except AttributeError:
        print('Вы не ввели требуемое количество числео')




import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot("5022959140:AAGqyGEkgyOxQgCbf5_RZkxdvvkdHZqJUfM")

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')





# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])

def handle_text(message):

    varTextMess = message.text
    
    # Если сообщение от пользователя
    if str(message.chat.id) != '-1001609885392':
        bot.send_message('-1001609885392', f'{message.chat.id}\n{message.text}')

    # Если сообщение получено аднимистрации
    if str(message.chat.id) == '-1001609885392':
        try:
            # Парсим chatId из сообщения 
            # Парсим текст сообщения без Chat id
            varId = re.match(r'[0-9]{5,20}', message.text)

            value1 = regexFun(message.text)

            bot.send_message(f'{varId.group(0)}', f'\n{value1[1]}')
        except AttributeError:
            bot.send_message('-1001609885392', f'Вы не заполнили userId')



        # varText = ''
        # bot.send_message('-1001609885392', f'Получено сообщение от администрации\n{message.text}')


# Запускаем бота
bot.polling(none_stop=True, interval=0)