from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Cria o teclado com botões inline para o menu principal
def teclado_principal():
    teclado = InlineKeyboardMarkup(row_width=2)
    botao_relatorio = InlineKeyboardButton("📊 Relatório", callback_data='relatorio')
    botao_despesas = InlineKeyboardButton("💸 Despesas", callback_data='despesas')
    botao_receitas = InlineKeyboardButton("💰 Receitas", callback_data='receitas')
    botao_historico = InlineKeyboardButton("📆 Histórico", callback_data='historico')
    botao_config = InlineKeyboardButton("🛠️ Configurações", callback_data='config')

    teclado.add(botao_relatorio, botao_despesas, botao_receitas, botao_historico, botao_config)
    return teclado


def teclado_categorias():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Alimentação", callback_data='cat_1'),
        InlineKeyboardButton("Transporte", callback_data='cat_2')
    )
    markup.row(
        InlineKeyboardButton("Saúde", callback_data='cat_3'),
        InlineKeyboardButton("Educação", callback_data='cat_4')
    )
    markup.row(
        InlineKeyboardButton("Lazer", callback_data='cat_5')
    )
    return markup
