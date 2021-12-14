# -*- coding: utf8 -*-

import telebot
from telebot import types, TeleBot
from email import message

bot: TeleBot = telebot.TeleBot('.............................')

KEY_TO_PHRASE = {
	'key_1': 'Овен\n\nЗалог Вашего счастья – Ваша семья. Они дают Вам ту опору и поддержку, что помогает в жизни. Цените их, ведь не каждому в жизни везет как Вам. Когда на Вашем пути встречаются проблемы, то идите на контакт к родным, это поможет Вам. Стоит задуматься над тем, что для счастья стоит отказаться от чего-то.',
	'key_2': 'Телец\n\nДля того, чтобы завоевать уважение окружающих, стоит изменить свое отношение к ним, проявляйте больше уважения. Вам стоит быть более сдержанным и позитивным. Если человек честен с Вами, то отвечайте ему тем же, это так редко можно встретить в наше время.',
	'key_3': 'Близнецы\n\nВ Вас эгоизма чуть больше, чем альтруизма, стоит менять в себе эту пропорцию. Да, уверенность в себе помогает Вам достигать многого в жизни, но не для всех такое поведение допустимо. Не тратьте свою внутреннюю энергию на ложь, она делает Вас слабее.',
	'key_4': 'Рак\n\nХудшее, что Вы можете сделать – это копить обиды и заставлять других обижаться. Если знаете, что человек обиделся на Вас, то лучше извиниться даже, если вы считаете себя правым в ситуации. Будьте собой, отпускайте ярлыки обид.',
	'key_5': 'Лев\n\nКонечно, важно иметь чувство собственного достоинства, но это может иметь и отрицательный эффект в жизни. Денежный вопрос занимает одну из первых позиций в Вашей жизни, но зачасту Вы живете не по средствам, научитесь вести учет средствам.',
	'key_6': 'Дева\n\nВ спорах Вы часто идете до конца, не задумываясь о том, что можете быть не правы. Это полезное качество в жизни, оно помогает двигаться по карьерной лестнице, но в личном общении может отталкивать людей.',
	'key_7': 'Весы\n\nНаучитесь прислушиваться к своему сердцу. Жизнь – сложная игра, в которой люди зачастую придумывают свои правила, но Вам выбирать по какому пути двигаться. Используйте чужое мнение, как совет, но точно не как единственно верное решение. Живите так, как чувствуете.',
	'key_8': 'Скорпион\n\nВы настолько уверены в себе, что часто отказываетесь от помощи других. Но люди делают это искренно, поэтому не нужно обижать их своим отказом. Также подумайте, прежде чем дать совет кому-то, потому что люди сделают неправильные выводы и будут винить Вас во всех бедах.',
	'key_9': 'Стрелец\n\nНаучитесь доверять людям, это сложно, но возможно. Люди, предлагая помощь, хотят помочь, цените это. У всех людей есть недостатки, поэтому не стоит считать себя во всем лучше других, станьте реалистом.',
	'key_10': 'Козерог\n\nВаше стремление быть идеальным заставляет Вас испытывать дискомфорт. Если у Вас что-то не получилось, то это не значит, что с Вами что-то не так, скорее всего есть другие причины. Вас успокаивает стабильность, но перемены случаются, и они не так страшны.',
	'key_11': 'Водолей\n\nПомните, что ценить людей мы начинаем только после утраты, поэтому не упускайте возможность сделать жизнь близкого лучше, ведь вы его любите. Так же не стоит возвышаться за счет принижения других, это не красит никого.',
	'key_12': 'Рыбы\n\nНайдите для себя в жизни то, что Вам приносит удовольствие и счастье и держитесь за это. Только, осознавая свои цели и желания можно поистине быть счастливым.'
}

@bot.message_handler(content_types=['text'])
def inline_key(a):
    if a.text == "Хочу гороскоп":
        mainmenu = types.InlineKeyboardMarkup( )
        key_1 = types.InlineKeyboardButton(text='♈️', callback_data='key_1')
        key_2 = types.InlineKeyboardButton(text='♉️', callback_data='key_2')
        key_3 = types.InlineKeyboardButton(text='♊️', callback_data='key_3')
        key_4 = types.InlineKeyboardButton(text='♋️', callback_data='key_4')
        key_5 = types.InlineKeyboardButton(text='♌️', callback_data='key_5')
        key_6 = types.InlineKeyboardButton(text='♍️', callback_data='key_6')
        key_7 = types.InlineKeyboardButton(text='♎', callback_data='key_7')
        key_8 = types.InlineKeyboardButton(text='️♏️️', callback_data='key_8')
        key_9 = types.InlineKeyboardButton(text='️♐️', callback_data='key_9')
        key_10 = types.InlineKeyboardButton(text='♑️', callback_data='key_10')
        key_11 = types.InlineKeyboardButton(text='♒', callback_data='key_11')
        key_12 = types.InlineKeyboardButton(text='♓', callback_data='key_12')
        mainmenu.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_10, key_11, key_12)
        bot.send_message(a.chat.id, 'Выбери свой знак зодиака...', reply_markup=mainmenu)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global text
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup( )
        key_1 = types.InlineKeyboardButton(text='♈️', callback_data='key_1')
        key_2 = types.InlineKeyboardButton(text='♉️', callback_data='key_2')
        key_3 = types.InlineKeyboardButton(text='♊️️', callback_data='key_3')
        key_4 = types.InlineKeyboardButton(text='♋️', callback_data='key_4')
        key_5 = types.InlineKeyboardButton(text='♌️', callback_data='key_5')
        key_6 = types.InlineKeyboardButton(text='♍️', callback_data='key_6')
        key_7 = types.InlineKeyboardButton(text='♎️', callback_data='key_7')
        key_8 = types.InlineKeyboardButton(text='♏️', callback_data='key_8')
        key_9 = types.InlineKeyboardButton(text='♐️', callback_data='key_9')
        key_10 = types.InlineKeyboardButton(text='♑️', callback_data='key_10')
        key_11 = types.InlineKeyboardButton(text='♒', callback_data='key_11')
        key_12 = types.InlineKeyboardButton(text='️♓', callback_data='key_12')
        mainmenu.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_10, key_11, key_12)
        bot.edit_message_text(text='Выбери свой знак зодиака...', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=mainmenu)
    else:
        next_menu = types.InlineKeyboardMarkup( )
        back = types.InlineKeyboardButton(text='✨', callback_data='mainmenu')
        next_menu.add(back)
        text = KEY_TO_PHRASE[call.data]
        bot.edit_message_text(chat_id=call.message.chat.id, text=text, message_id=call.message.message_id, reply_markup=next_menu)

bot.polling(none_stop=True, interval=0)
