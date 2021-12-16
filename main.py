import telebot
from telebot import types, TeleBot

import config

from keyboards import zodiac_menu, cookies_menu, back_menu_def
from keys_to_phrases import KEYS_TO_ZODIAC_SIGNS, KEYS_TO_COOKIES

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['go', 'start'])  # command handler for /start
def welcome(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать!\nНапиши мне «Хочу гороскоп», если хочешь почитать о своем знаке зодиака, '
                     'или «Хочу предсказание», если хочешь вытянуть печеньку с предсказанием')


@bot.message_handler(content_types=['text'])
def msg_handler(message):
    if message.text.lower() == 'хочу гороскоп':
        # request handler for horoscope
        bot.send_message(message.chat.id, 'Выбери свой знак зодиака...', reply_markup=zodiac_menu)

    elif message.text.lower() == 'хочу предсказание':
        # request handler for predictions
        bot.send_message(message.chat.id, 'Выбери печеньку...', reply_markup=cookies_menu)

    else:
        bot.send_message(message.chat.id, 'Не понял тебя :(\nНажми /go')


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data in ('zodiac_menu', 'cookies_menu'):
        # return handler
        bot.edit_message_text(
            text='Выбери свой знак зодиака...' if call.data == 'zodiac_menu' else 'Выбери печеньку...',
            chat_id=call.message.chat.id, message_id=call.message.message_id,
            reply_markup=zodiac_menu if call.data == 'zodiac_menu' else cookies_menu)

    elif call.data in KEYS_TO_COOKIES.keys():
        # handler for keys from menu with predictions
        back_menu = back_menu_def('cookies_menu')
        text_c = KEYS_TO_COOKIES[call.data]
        bot.edit_message_text(chat_id=call.message.chat.id, text=text_c,
                              message_id=call.message.message_id, reply_markup=back_menu)

    elif call.data in KEYS_TO_ZODIAC_SIGNS.keys():
        # handler for keys from menu with horoscope
        back_menu = back_menu_def('zodiac_menu')
        text_a = KEYS_TO_ZODIAC_SIGNS[call.data]
        bot.edit_message_text(chat_id=call.message.chat.id, text=text_a,
                              message_id=call.message.message_id, reply_markup=back_menu)




bot.polling(none_stop=True, interval=0)
