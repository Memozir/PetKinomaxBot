from dispatcher import dp, bot
from . callback_factory import cb
import keyboards
from kinomax.kinomax_parser import result
from states import MessageNumber


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

import re


@dp.callback_query_handler(cb.filter(), state=MessageNumber.SAVE_ID)
async def bot_functions(query: types.CallbackQuery, callback_data: dict, state: FSMContext):

	await bot.answer_callback_query(query.id)

	id = callback_data['id']
	show_hide_check = re.split('_', id)[0]

	if id == 'parse':

		await bot.send_message(query['message']['chat']['id'], 'Это может занять несколько секунд') # user friendly message
		# await state.reset_data()

		films = result()
		films = keyboards.add_btn(films)

		data = await state.get_data()
		user_friendly_message_id = data['find_film_count'] + query['message']['message_id'] + 1

		id_count = 1
		for film in films:
			film['chat_id'] = query['message']['from']['id']
			film['message_id'] = user_friendly_message_id + id_count
			id_count += 1

		#updating the data in state
		await state.update_data(movies = films)

		if len(films) == 0:

			await bot.send_message(query.from_user.id, 'На данный момент в Киномаксе нет сеансов')

		else:

			id_count = 0
			for film in films:

				await bot.send_message(
                    query.from_user.id, 
					f'<b>{film["title"]}</b>\n' + 
                    f'\nСеансы:\n{film["time"]}' + 
                    hlink('купить билет\n'.upper(), film["buy"]),
					disable_web_page_preview=True,
                    reply_markup=film['kb_show']
                    )


	if id == 'find_film':
		await bot.send_message(query.from_user.id, 'Данная функция находится в разработке')
		data = await state.get_data()
		find_film_count = data['find_film_count']
		find_film_count += 1
		await state.update_data(find_film_count = find_film_count)

	elif show_hide_check == 'show':

		films = await state.get_data()

		for film in films['movies']:

			if id == film['id_show']:

				# I have to collect message_id in states
				# The line below is working how it must works, use it
				await bot.edit_message_text(chat_id=query['message']['chat']['id'], message_id=film['message_id'],
					text=film['discription'], reply_markup=film['kb_hide'])

	elif show_hide_check == 'hide':

		films = await state.get_data()

		for film in films['movies']:
			if id == film['id_hide']:
				await bot.edit_message_text(
                    chat_id=query['from']['id'],
                    message_id=film['message_id'],
					text=f'<b>{film["title"]}</b>\n' + 
                    f'\nСеансы:\n{film["time"]}' + 
                    hlink('купить билет\n'.upper(), film["buy"]),
					disable_web_page_preview=True,
                    reply_markup=film['kb_show']
                    )
