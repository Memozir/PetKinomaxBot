from dispatcher import dp, bot
from aiogram import types
import keyboards
from text import messages
from states import MessageNumber
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='start', state='*')
async def start_message(message: types.Message):
	await message.answer(messages.start['start_message'], reply_markup=keyboards.kb_start)


@dp.message_handler(state='*')
async def display_func(message: types.Message, state: FSMContext):
	if message.text.lower() == 'начать':
		await state.update_data(find_film_count = 0)
		await MessageNumber.SAVE_ID.set()
		await message.answer('Выберите, что хотите сделать:', reply_markup=keyboards.kb_func)
