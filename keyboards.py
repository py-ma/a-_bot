# -*- coding: utf-8 -*-
from telebot import types

zodiac_menu = types.InlineKeyboardMarkup()
zodiac_key_1 = types.InlineKeyboardButton(text='♈️', callback_data='zodiac_key_1')
zodiac_key_2 = types.InlineKeyboardButton(text='♉️', callback_data='zodiac_key_2')
zodiac_key_3 = types.InlineKeyboardButton(text='♊️', callback_data='zodiac_key_3')
zodiac_key_4 = types.InlineKeyboardButton(text='♋️', callback_data='zodiac_key_4')
zodiac_key_5 = types.InlineKeyboardButton(text='♌️', callback_data='zodiac_key_5')
zodiac_key_6 = types.InlineKeyboardButton(text='♍️', callback_data='zodiac_key_6')
zodiac_key_7 = types.InlineKeyboardButton(text='♎', callback_data='zodiac_key_7')
zodiac_key_8 = types.InlineKeyboardButton(text='️♏️️', callback_data='zodiac_key_8')
zodiac_key_9 = types.InlineKeyboardButton(text='️♐️', callback_data='zodiac_key_9')
zodiac_key_10 = types.InlineKeyboardButton(text='♑️', callback_data='zodiac_key_10')
zodiac_key_11 = types.InlineKeyboardButton(text='♒', callback_data='zodiac_key_11')
zodiac_key_12 = types.InlineKeyboardButton(text='♓', callback_data='zodiac_key_12')
zodiac_menu.add(zodiac_key_1, zodiac_key_2, zodiac_key_3, zodiac_key_4, zodiac_key_5, zodiac_key_6,
                zodiac_key_7, zodiac_key_8, zodiac_key_9, zodiac_key_10, zodiac_key_11, zodiac_key_12)


cookies_menu = types.InlineKeyboardMarkup()
cookies_key_1 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_1')
cookies_key_2 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_2')
cookies_key_3 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_3')
cookies_key_4 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_4')
cookies_key_5 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_5')
cookies_key_6 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_6')
cookies_key_7 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_7')
cookies_key_8 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_8')
cookies_key_9 = types.InlineKeyboardButton(text='🍪', callback_data='cookies_key_9')
cookies_menu.add(cookies_key_1, cookies_key_2, cookies_key_3, cookies_key_4, cookies_key_5,
                 cookies_key_6, cookies_key_7, cookies_key_8, cookies_key_9)


def back_menu_def(direction):
    back_menu = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='✨', callback_data=direction)
    back_menu.add(back)
    return back_menu
