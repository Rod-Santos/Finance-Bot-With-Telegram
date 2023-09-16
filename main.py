from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from actions import despesas
from dotenv import load_dotenv
import logging
import os

# Initialize bot and dispatcher
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.callback_query_handler(lambda c: c.data == 'despesas')
async def process_callback_despesas(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    state = FSMContext(dp.storage, callback_query.from_user.id, callback_query.message.chat.id)
    await despesas.handle(callback_query, state)

@dp.message_handler(state=despesas.Despesa.descricao)
async def process_descricao(message: types.Message, state: FSMContext):
    await despesas.descricao_despesa(message, state)

@dp.message_handler(state=despesas.Despesa.valor)
async def process_valor(message: types.Message, state: FSMContext):
    await despesas.valor_despesa(message, state)

@dp.message_handler(state=despesas.Despesa.categoria)
async def process_categoria(message: types.Message, state: FSMContext):
    await despesas.categoria_despesa(message, state)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
