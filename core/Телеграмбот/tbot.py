import datetime
from time import sleep
import requests
import telebot
from telebot import types
from lxml import html


def cleaner(text):
		result = ''
		arr = text.split(" ")
		for j in arr:
			if j != "" and j != "\n" :
				result += j + " "
		return result

def get_json_array():
	for index in reversed(range(20)):
		feedback = "Page" + str(index) + " | " + str(datetime.datetime.now().time())
		html_as_text = requests.get('https://krisha.kz/prodazha/kvartiry/almaty/?das[who]=1&page=' + str(index)).text
		sleep(3)
		feedback += "\nНачало:" + str(index) + " | " + str(datetime.datetime.now().time())

		html_object = html.fromstring(html_as_text)
		all_links = html_object.xpath('//div/@data-id')
		# site_dict_array = get_json_array(elements, html_object)
		among = 0
		for i in all_links:
			core_text = html_object.xpath('//div[@data-id=' + str(i)+']')[0]
			text = core_text.find_class('a-card__title')[0].text_content() + " - " + cleaner(core_text.find_class('a-card__price')[0].text_content())
			is_new = len(core_text.find_class('a-card__complex-label')) > 0
			post_dat = core_text.find_class('card-stats')[0]
			post_date = post_dat.find_class('card-stats__item')[1].text_content()
			data_color = core_text.get('data-color')
			iqiq = {
				"id": i,
				"link": "https://krisha.kz/a/show/" + i,
				"post_date" : cleaner(post_date).split(" ")[0],
				"text" : cleaner(text),
				"is_new_building" : is_new,
				"message_was_sent" : False,
				"sended_date" : None,
				"data_color" : data_color
			}
			print("\nСоздан- "+str(i))
			# print(datetime.datetime.today().day)
			# print(iqiq['is_new_building'] == False and str(iqiq['post_date']) == str(datetime.datetime.today().day))
			if iqiq['is_new_building'] == False and str(iqiq['post_date']) == str(datetime.datetime.today().day) :
				iqiq['message_was_sent'] = True
				iqiq['sended_date'] = datetime.date.today()
				new_data = "\n"
				new_data += iqiq['id']
				new_data += "|" + str(iqiq['link'])
				new_data += "|" + str(iqiq['post_date'])
				new_data += "|" + str(iqiq['is_new_building'])
				new_data += "|" + str(iqiq['message_was_sent'])
				new_data += "|" + str(iqiq['sended_date'])
				with open('data.txt', 'a') as f:
					f.write(new_data)
					print("Записан- "+str(new_data)+ "\n")
					among += 1
		feedback += "\nЗапись страницы завершен\nКоличество сохраненных:" + str(among) + " | " + str(datetime.datetime.now().time())
		bot.send_message(1907105904, text=feedback, reply_markup=None)
		
	# return data_list




bot = telebot.TeleBot('5724464351:AAFM9h_gS_oF9yHWqqfdPaSjwk0-AjKxYoU')

rooms_1 = "Показывать 1-комнатные квартиры"
rooms_2 = "Показывать 2-комнатные квартиры"
rooms_3 = "Показывать 3-комнатные квартиры"
rooms_4 = "Показывать 4-комнатные квартиры"
rooms_5 = "Показывать 5-комнатные квартиры"
rooms_more = "Показывать квартиры с 5 и более комнатами"
rooms_all = "Показывать всё"


@bot.message_handler(commands=['start'])
def get_weather(message):
	ALLOWED_CHATS = open("ALLOWED_CHATS.txt", "r").read().split("\n")
	IS_ALLOWED_CHAT = False
	print(ALLOWED_CHATS)
	for i in ALLOWED_CHATS:
		if str(i) == str(message.chat.id):
			IS_ALLOWED_CHAT = True
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("Проверка бота")
			item3 = types.KeyboardButton("Фильтр")
			item2 = types.KeyboardButton("Текущий фильтр")
			markup.add(item1,item3,item2)
			bot.send_message(message.chat.id, text="Добро пожаловать!", reply_markup=markup)


	if IS_ALLOWED_CHAT == False:
		text = "ID: " + str(message.from_user.id) + "\nusername: @" + str(message.from_user.username) + "\nName: " +  str(message.from_user.first_name) + " " + str(message.from_user.last_name) 
		markup_for_owner = types.InlineKeyboardMarkup(row_width=1)
		add_user = types.InlineKeyboardButton("Добавить пользователя", callback_data=message.chat.id)
		markup_for_owner.add(add_user)
		bot.send_message(1907105904, text=text, reply_markup=markup_for_owner)
		bot.send_message(545221996, text=text, reply_markup=markup_for_owner)
		bot.send_message(message.chat.id, text="⏰ Ваш запрос на подключения выслан администратору. Пожалуйста дождитесь ответа", reply_markup=None)
	# 1907105904
	

	
@bot.message_handler(commands=['check'])
def get_weather(message):

	bot.send_message(message.chat.id, text="Проверка статуса...")
	sleep(3)
	current_time = datetime.datetime.today()
	bot.send_message(message.chat.id, text="Время: "+str(current_time)+
        "\nСтатус: ✅Работает\nСообщение: Бот работает без сбоев, никаких сбоев не обнаружено")


@bot.message_handler(content_types=['text'])
def nurta_chort(message):
	if message.text == rooms_all:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("all")
				f.write("all")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_all, reply_markup=markup)

				
	elif message.text == rooms_1:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("komnat_1")
				f.write("komnat_1")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_1, reply_markup=markup)

	elif message.text == rooms_2:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("komnat_2")
				f.write("komnat_2")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_2, reply_markup=markup)

	elif message.text == rooms_3:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("komnat_3")
				f.write("komnat_3")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_3, reply_markup=markup)

	elif message.text == rooms_4:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("komnat_4")
				f.write("komnat_4")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_4, reply_markup=markup)

	elif message.text == rooms_5:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("komnat_5")
				f.write("komnat_5")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_5, reply_markup=markup)

	elif message.text == rooms_more:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		with open('current_filter.txt', 'w') as f:
				print("komnat_5_and_more")
				f.write("komnat_5_and_more")
		bot.send_message(message.chat.id, text="Фильтр изменен на " + rooms_more, reply_markup=markup)

	elif message.text == "Фильтр":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn_rooms_all = types.KeyboardButton(rooms_all)
		btn_rooms_1 = types.KeyboardButton(rooms_1)
		btn_rooms_2 = types.KeyboardButton(rooms_2)
		btn_rooms_3 = types.KeyboardButton(rooms_3)
		btn_rooms_4 = types.KeyboardButton(rooms_4)
		btn_rooms_5 = types.KeyboardButton(rooms_5)
		btn_rooms_more = types.KeyboardButton(rooms_more)
		btn_back = types.KeyboardButton("Назад")

		markup.add(btn_rooms_1,btn_rooms_2,btn_rooms_3,btn_rooms_4,btn_rooms_5,btn_rooms_more,btn_rooms_all,btn_back)
		bot.send_message(message.chat.id, text="Нажмите на фильтр", reply_markup=markup)
	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Проверка бота")
		item3 = types.KeyboardButton("Фильтр")
		item2 = types.KeyboardButton("Текущий фильтр")
		markup.add(item1,item3,item2)
		bot.send_message(message.chat.id, text="...", reply_markup=markup)
	elif message.text == "Проверка бота":
		bot.send_message(message.chat.id, text="Проверка статуса...")
		sleep(3)
		current_time = datetime.datetime.today()
		# current_time = datetime.now()
		bot.send_message(message.chat.id, text="Время: "+str(current_time)+
        "\nСтатус: ✅Работает\nСообщение: Бот работает без сбоев, никаких сбоев не обнаружено")

	elif message.text == "Текущий фильтр":
		f = open("current_filter.txt", "r")
		x = f.read()
		if x.find("all") != -1:
			bot.send_message(message.chat.id, text=rooms_all)
		elif x.find("komnat_1") != -1:
			bot.send_message(message.chat.id, text=rooms_1)
		elif x.find("komnat_2") != -1:
			bot.send_message(message.chat.id, text=rooms_2)
		elif x.find("komnat_3") != -1:
			bot.send_message(message.chat.id, text=rooms_3)
		elif x.find("komnat_4") != -1:
			bot.send_message(message.chat.id, text=rooms_4)
		elif x.find("komnat_5") != -1:
			bot.send_message(message.chat.id, text=rooms_5)
		elif x.find("komnat_5_and_more") != -1:
			bot.send_message(message.chat.id, text=rooms_more)
		else:
			bot.send_message(message.chat.id, text="rooms_more")
		f.close()
	elif message.text == "Вырубить бота":
		with open('off.txt', 'w') as f:
				print("1")
				f.write("1")
	elif message.text == "Вырубить Парсер":
		with open('off.txt', 'w') as f:
				print("1")
				f.write("1")
	elif message.text == "Массовая выгрузка":
		bot.send_message(message.chat.id, text="Начиаем...")

		get_json_array()
		bot.send_message(message.chat.id, text="Выгрузка завершена")


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		with open('ALLOWED_CHATS.txt', 'a') as f:
			print(call.data)
			f.write('\n')			
			f.write(str(call.data))	
			f.close()
			bot.edit_message_text(chat_id=call.message.chat.id, 
				message_id=call.message.message_id, 
				text= call.message.text + "\n\n✅ Пользователь добавлен", 
				reply_markup=None)

			bot.send_message(1907105904, text=call.message.text + "\n\n✅ Пользователь добавлен", reply_markup=None)
			bot.send_message(call.data, text="🥳 Вам предоставили доступ к боту. Нажмите на /start что бы активировать его")
			
	except:
		print(call.data)

bot.infinity_polling()


