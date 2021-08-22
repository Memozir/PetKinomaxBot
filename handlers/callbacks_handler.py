from dispatcher import dp, bot
from . callback_factory import cb
from aiogram import types
from kinomax_parser import result
from aiogram.utils.markdown import hlink


@dp.callback_query_handler(cb.filter())
async def bot_functions(query: types.CallbackQuery, callback_data: dict):

	await bot.answer_callback_query(query.id)

	id = callback_data.get('id')

	if id == 'parse':
		films = result()

		if len(films) == 0:
			await bot.send_message(query.from_user.id, 'На данный момент в Киномаксе нет сеансов')
		else:
			for film in films:
				await bot.send_message(query.from_user.id, f'Фильм: {film["title"].upper()}\n' + hlink('Купить билет'.upper(), film["buy"]), disable_webpage_preview=True)

	elif id == 'find_film':
		await bot.send_message(query.from_user.id, 'Данная функция находится в разработке')
