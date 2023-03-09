from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
InlineKeyboardMarkup, InlineKeyboardButton
from handlers.callback_factory import cb


# Start keyboard
kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
btn_start = KeyboardButton('Начать')
kb_start.add(btn_start)

# Functions keyboard
kb_func = InlineKeyboardMarkup(row_width=1)
btn_parse = InlineKeyboardButton(text='Афиша в кинотеатре', callback_data=cb.new(id='parse'))
# btn_find_film = InlineKeyboardButton(text='Найти фильм', callback_data=cb.new(id='find_film'))
kb_func.add(btn_parse)

# Geolocation
btn_geo = KeyboardButton('Поделиться геопозицией', request_location=True)
geo_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_geo)

# Show\Hide discription
def add_btn(films):

	count = 0

	for film in films:
		
		film['id_show'] = f'show_{count}'
		film['id_hide'] = f'hide_{count}'
		film['kb_show'] = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Описание', row_width=1, callback_data=cb.new(id=f'show_{count}')))
		film['kb_hide'] = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Назад', row_width=1, callback_data=cb.new(id=f'hide_{count}')))
		count += 1

	return films