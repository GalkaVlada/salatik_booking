import telebot;
bot = telebot.TeleBot('1435978036:AAGmJOMQv4q89TU0q8Qinq8fSDkdoiFSJYo');
#weRtr_bot

@bot.message_handler(commands=['start'])
def start(m):
    print(m.chat.id)
    bot.send_message(m.chat.id,'Hello! \n /size for setting size of room \n')
    bot.register_next_step_handler(m, picker)
def picker(m):#выбираем че зотим делать в принципе
    if m.text=='/size':
        bot.send_message(m.chat.id,'выбери свой размер')
        bot.register_next_step_handler(m, sizePick)
    else:
        bot.send_message(m.chat.id,'/help to узнать шо происходит')
def sizePick(m):#выбор размера комнаты
    num = m.text.lower()
    bot.send_message(m.chat.id,'окей, пайехоле дальши')
    try:
        maxAmount = int(num)
        bot.send_message(m.chat.id,'окей, пайехоле дальши')
        bot.register_next_step_handler(m, grabber, maxAmount)
    except BaseException:
        bot.send_message(m.chat.id,'не то ввел, пробуем еще раз(/try) или ну его?(/start)')
        bot.register_next_step_handler(m, sizePickException)

def sizePickException(m):#не попал по кнопкам когда вводил размер комнаты
        if m.text=='/try':
            bot.register_next_step_handler(m, sizePick)
        elif m.text == '/start':
            bot.register_next_step_handler(m, start)
        else:
            bot.register_next_step_handler(m, sizePickException)
def grabber(m, maxAmount):#плюсики ловим
    if m.text=='+':
        ID = m.from_user.id
        if ID in added:
            bot.register_next_step_handler(m, grabber)
        else:
            if len(added)>=maxAmount:
                bot.send_message(m.chat.id,'а всеее, а надо было раньше\n\n\nеще хз куда отправлять')
                #зависит от структуры бота, надо обсудить, суперпозиция с верхней строчкой
            else:
                added.append(ID)
                bot.send_message(m.chat.id,str(m.from_user.username)+' записался на митинг(свергнем царя нашего, Лукашеночку!)')
                bot.register_next_step_handler(m, grabber)

'''а н это ваще можно забить |||||||def 
    if m.text.lower() == '+':
        if len(added)>=maxAmount:
        bot.send_message(m.from_user.id,'hi!')
    elif m.text.lower() == '/help':
        bot.send_message(m.from_user.id,'smth like if u want to book place print +')
    else:
        bot.send_message(m.from_user.id,'u are an idiot. Do you agree? Print /help')
'''
bot.polling(none_stop=True, interval=1)
