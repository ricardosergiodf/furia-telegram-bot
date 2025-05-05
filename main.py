import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.config import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(msg):
    bot.reply_to(msg, SAUDACAO_OUT)

@bot.message_handler(commands=['comandos'])
def comandos(msg):
    texto = "Comandos disponíveis:\n" + "\n".join(COMANDOS_DISPONIVEIS)
    bot.reply_to(msg, texto)

@bot.message_handler(commands=['historia'])
def historia(msg):
    bot.reply_to(msg, HISTORIA)

@bot.message_handler(commands=['times'])
def times(msg):
    markup = InlineKeyboardMarkup()
    for key in LINEUPS:
        texto_botao = LINEUPS[key][0]  # botão com emoji
        markup.add(InlineKeyboardButton(text=texto_botao, callback_data=key))
    bot.send_message(msg.chat.id, "Escolha um time para ver a line atual:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_times(call):
    nome_time = call.data
    resposta = LINEUPS.get(nome_time, ('', 'Time não encontrado.'))[1]
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, resposta)

@bot.message_handler(commands=['redes_sociais'])
def redes_sociais(msg):
    texto = "Redes Sociais da Furia\n" + "\n".join(REDES_SOCIAIS)
    bot.reply_to(msg, texto)

@bot.message_handler(commands=['conquistas'])
def conquistas(message):
    texto = "🏆 *Conquistas Notáveis da FURIA:*\n\n"
    for nome, (posicao, detalhes) in CONQUISTAS.items():
        texto += f"{posicao} — {nome}\n{detalhes}\n\n"
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: msg.text is not None)
def responder(msg):
    texto = msg.text.lower()

    # Em grupos: só responde se for mencionado
    if msg.chat.type in ['group', 'supergroup']:
        if BOT_USERNAME.lower() in texto:
            texto_sem_mencao = texto.replace(BOT_USERNAME.lower(), '').strip()
            responder_texto(msg, texto_sem_mencao)

    # Em privado: responde sempre
    elif msg.chat.type == 'private':
        responder_texto(msg, texto)

# Função que define as respostas
def responder_texto(msg, texto):
    if texto in SAUDACAO_IN:
        bot.reply_to(msg, SAUDACAO_OUT)
    elif texto in DESPEDIDA_IN:
        bot.reply_to(msg, DESPEDIDA_OUT)
    elif texto == 'comandos':
        bot.reply_to(msg, "Comandos disponíveis:\n" + "\n".join(COMANDOS_DISPONIVEIS))
    else:
        bot.reply_to(msg, "Não consegui entender sua mensagem. Digite /help para ajuda")

bot.infinity_polling()