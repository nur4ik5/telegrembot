import telebot
from main import get_titles

bot = telebot.TeleBot('1953071848:AAGkfgAupXUTpKoiIag1ZIf9sylfQRyAn84')

@bot.message_handler(commands=['start','старт'])
def send_welcome(message):
	bot.reply_to(message,'Привет. Чем могу помочь?')

# бот отвечает тебе что ты написал  
# @bot.message_handler(func=lambda m: True)
# def parrot(message):
# 	bot.reply_to(message, message.text)

@bot.message_handler(commands=['picture'])
def send_pic(message):
	chat_id = message.chat.id
	# bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
	bot.send_photo(chat_id=chat_id, photo=open('123.jpg', 'rb'))


@bot.message_handler(commands=['кутман'])
def send_kut(message):
	chat_id = message.chat.id
	
	bot.send_photo(chat_id=chat_id, photo=open('5.jpg', 'rb'))


@bot.message_handler(commands=['сайлоо'])
def send_kut(message):
	chat_id = message.chat.id
	
	bot.send_photo(chat_id=chat_id, photo=open('l.jpg', 'rb')) 
 


@bot.message_handler(commands=['series'])
def send_series(message):
	pass
	bot.reply_to(message, '\n'.join(get_titles()))


bot.polling()