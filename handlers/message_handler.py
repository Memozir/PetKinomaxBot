from dispatcher import dp, bot
from aiogram import types
import keyboards
from text import messages


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
	await message.answer(messages.start['start_message'], reply_markup=keyboards.kb_start)


@dp.message_handler(commands='geo')
async def get_geo(message: types.Message):
	await message.answer('Э, дай геолокацию!', reply_markup=keyboards.geo_kb)


@dp.message_handler()
async def display_func(message: types.Message):
	if message.text.lower() == 'начать':
		await message.answer('Выберите, что хотите сделать:', reply_markup=keyboards.kb_func)


