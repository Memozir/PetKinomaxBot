from aiogram.dispatcher.filters.state import State, StatesGroup


class MessageNumber(StatesGroup):

	SAVE_ID = State()
	PARSE = State()
	FIND_FILM = State()
