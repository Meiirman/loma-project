import datetime
from time import sleep
import requests
import telebot
from telebot import types
import json

bot = telebot.TeleBot('5041015087:AAGQpkjpbS6Pz2yCVOUHcDcQUOKSf-WqfpA')

@bot.message_handler(commands=['start'])
def get_weather(message):
	COURIERS_REQUESTS = open("core/couriers_requests.txt", "r").read().split("\n")
	IS_IN_COMAPNY = False
	for i in COURIERS_REQUESTS:
		if str(i).split("|")[0] == str(message.chat.id):
			IS_IN_COMAPNY = True


	if IS_IN_COMAPNY == False:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Подать запрос")
		markup.add(item1)
		bot.send_message(message.chat.id, text="Добро пожаловать курьер! Нажмите на кнопку \"Подать запрос\" что бы администраторм мог вас добавить в систему", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, text="Вы уже подключены", reply_markup=None)
	# 1907105904
	

	
@bot.message_handler(commands=['check'])
def get_weather(message):
	pass

@bot.message_handler(content_types=['text'])
def podanzapros(message):
	if message.text == "Подать запрос":
		with open('core/couriers_requests.txt', 'a') as f:
			text = str(message.chat.id)
			text += "|" + str(message.chat.username)
			text += "|" + str(message.chat.first_name)
			text += "|" + str(message.chat.last_name)
			text += "|" + str("False\n")
			f.write(text)
		bot.send_message(message.chat.id, text="Запрос был отправлен администратору. Когда администратор примет ваш запрос мы вам сообщим", reply_markup=None)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		with open('change_data.txt', 'w') as f:
			print(call.data)
			f.write(str(call.data))	
			f.close()
			bot.edit_message_text(chat_id=call.message.chat.id, 
				message_id=call.message.message_id, 
				text= "✅ Этап был изменен\n\n" + call.message.text, 
				reply_markup=None)

			# bot.send_message(1907105904, text=call.message.text + "\n\n✅ Пользователь добавлен", reply_markup=None)
			# bot.send_message(call.data, text="🥳 Вам предоставили доступ к боту. Нажмите на /start что бы активировать его")
			
	except:
		print(call.data)

bot.infinity_polling()


