import telebot
import random
import time
import schedule
import threading
import datetime

print("Успішний імпорт бібліотек")

# Создаем экземпляр бота
bot = telebot.TeleBot('5349715079:AAGxtfeDKtTXyf6y3T4DCQNRjQbfg0W_70Q')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '🥳 Уррра тепер ти з нами')

@bot.message_handler(commands=["status"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Все ок')
    time11 = datetime.datetime.now()
    bot.send_message(m.chat.id, time11)





def hh23(): 
    print("HH 23")
    texts = "Урок ШАГ чере годину пора вдіватися"
    send(texts)


def slep1(): 
    print("Slep1")
    texts = random.choice(["Або ти лягаєш спати, або Ванга прокляне.", "Бистренько в ліжечко ато мішка фреді цапне за пяточку", "Бистро спать!"])
    bot.send_message(650550237, texts)
    bot.send_message(702959203, texts)






def send(texts, data_url):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Перейти у відеодзвінок', url=data_url))
    markup.add(telebot.types.InlineKeyboardButton(text='Потеряйся', callback_data=1))
    id1 = bot.send_message(650550237, text=texts, reply_markup=markup).message_id
    id2 = bot.send_message(702959203, text=texts, reply_markup=markup).message_id
    
    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        bot.answer_callback_query(callback_query_id=call.id, text='Біп-пу-пі')
        if call.data == '1':
            if call.message.chat.id == 650550237:
                bot.delete_message(650550237, id1)
                id3 = bot.send_message(650550237, '😎 Дематеріалізовуюсь').message_id
                time.sleep(2)
                bot.delete_message(650550237, id3)
            else:
                bot.delete_message(702959203, id2)
                id4 = bot.send_message(702959203, '😎 Дематеріалізовуюсь').message_id
                time.sleep(2)
                bot.delete_message(702959203, id4)
        


schedule.every().saturday.at("09:00").do(hh23)


schedule.every().monday.at("20:00").do(slep1)
schedule.every().tuesday.at("20:00").do(slep1)
schedule.every().wednesday.at("20:00").do(slep1)
schedule.every().thursday.at("20:00").do(slep1)
schedule.every().friday.at("20:00").do(slep1)
schedule.every().saturday.at("20:00").do(slep1)
schedule.every().sunday.at("20:00").do(slep1)

def background():
    while True:
        print("Тик")
        schedule.run_pending()
        time.sleep(10)
        
        

b = threading.Thread(name='background', target=background)
b.start()

bot.polling(none_stop=True, interval=0)