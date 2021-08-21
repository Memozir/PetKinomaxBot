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
btn_find_film = InlineKeyboardButton(text='Найти фильм', callback_data=cb.new(id='find_film'))
kb_func.add(btn_parse, btn_find_film)