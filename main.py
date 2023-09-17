from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Text
from menus import teclado_principal  
from actions import despesas  
from actions.despesas import Despesa  
import logging
from database import insert_user  # Importe a função aqui

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)




@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name  # Obtém o nome completo do usuário
    insert_user(user_id, user_name)  # Passe o nome como um segundo argumento
    
    markup = teclado_principal()  # Chamada da função para obter o InlineKeyboardMarkup
    
    await message.reply("Olá! Como posso ajudá-lo hoje?", reply_markup=markup)



@dp.callback_query_handler(lambda c: c.data == 'despesas')
async def process_callback_despesas(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    state = FSMContext(dp.storage, callback_query.from_user.id, callback_query.message.chat.id)
    await despesas.handle(callback_query, state)



@dp.message_handler(state=Despesa.descricao)
async def process_descricao(message: types.Message, state: FSMContext):
    await despesas.descricao_despesa(message, state)

@dp.message_handler(state=Despesa.valor)
async def process_valor(message: types.Message, state: FSMContext):
    await despesas.valor_despesa(message, state)

@dp.message_handler(state=Despesa.categoria)
async def process_categoria(message: types.Message, state: FSMContext):
    await despesas.categoria_despesa(message, state)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
