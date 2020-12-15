import telebot

bot = telebot.TeleBot('1459400031:AAErKHA4GNZmE8aRIvvf2_kyWhWGp5-Xyfk')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет,Дружище.Ты написал мне /start')

import telebot



TELEGRAM_TOKEN = "token"

bot = telebot.TeleBot(TELEGRAM_TOKEN)



@bot.message_handler(content_types=['text'])

def send_text(message):

    if message.text == 'Hi':

         bot.send_message(message.chat.id, 'Hello')



    elif message.text == 'Who is your creatore?':
        bot.send_message(message.chat.id, 'Your name')


    else:
        atext = message.text[:3] + message.text.lower()
        bot.send_message(message.chat.id, atext)

bot.polling()