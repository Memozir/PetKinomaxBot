from aiogram import Dispatcher, Bot, types
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def shutdow(dispatcher: Dispatcher):
	await dispatcher.storage.close()
	await dispatcher.storage.wait_closed()


# async def bot_start(state: FSMContext):
# 	await MessageNumber.SAVE_ID.set()
# 	await state.update_data(find_film_count = 0)
# 	await state.reset_state(with_data=False)