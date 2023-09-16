from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import insert_despesa, get_all_categories

class Despesa(StatesGroup):
    descricao = State()
    valor = State()
    categoria = State()

async def iniciar_despesa(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    await query.message.reply("Por favor, digite a descrição da despesa:")
    await Despesa.descricao.set()

async def descricao_despesa(message: types.Message, state: FSMContext):
    descricao = message.text
    await state.update_data(descricao=descricao)
    await message.reply("Por favor, digite o valor da despesa:")
    await Despesa.valor.set()

async def valor_despesa(message: types.Message, state: FSMContext):
    valor = message.text.replace(',', '.')
    await state.update_data(valor=valor)
    
    categories = get_all_categories()
    categories_str = "\n".join([f"{c[0]} - {c[1]}" for c in categories])
    
    await message.reply(f"Valor adicionado. Por favor, escolha uma categoria para essa despesa:\n{categories_str}")
    await Despesa.categoria.set()

async def categoria_despesa(message: types.Message, state: FSMContext):
    categoria_id = int(message.text)
    data = await state.get_data()
    valor = data.get("valor")
    
    if valor is None:
        await message.reply("Desculpe, não consegui encontrar o valor da despesa. Vamos tentar novamente.")
        return
    
    valor = float(valor.replace(',', '.'))
    usuario_id = message.from_user.id
    
    insert_despesa(valor, categoria_id, usuario_id)
    
    descricao = data.get("descricao")
    await message.reply(f"Despesa adicionada:\nDescrição: {descricao}\nValor: {valor}\nCategoria ID: {categoria_id}")
    await state.finish()

async def handle(query: types.CallbackQuery, state: FSMContext):
    await iniciar_despesa(query, state)
