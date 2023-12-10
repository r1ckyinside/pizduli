import telebot
import sqlite3
from telebot import types
from importfromdata import meme
from importfromusers import contacts
from random import randint

bot = telebot.TeleBot("6957840347:AAHwUYKl59mWjqOBheue5IMj_CsFxU3pykc")
con = sqlite3.connect("data.sqlite3", check_same_thread=False)
cur = con.cursor()

def add_bd(usermeme):
    cur.execute('''INSERT INTO meme VALUES (?)''', (usermeme,))
    con.commit()
    update_bd()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет! Я помогу обосрать любого бездаря!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Привет":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выбрать бездаря")
        btn2 = types.KeyboardButton("Сгенерировать подъеб")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Привет! Я помогу обосрать любого бездаря!", reply_markup=markup)

    elif message.text == "Выбрать бездаря":
        markup = types.InlineKeyboardMarkup()
        i = 0
        for i in range(contacts().__len__()):
            item = types.InlineKeyboardButton(text=contacts()[i][0], url=contacts()[i][1])
            markup.add(item)
        add_user = types.InlineKeyboardButton(text="Добавить пользователя", callback_data='add_user')
        markup.add(add_user)
        bot.send_message(message.from_user.id, "Выбери кому дать пизды", reply_markup=markup)

    elif message.text == "Сгенерировать подъеб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выбрать бездаря")
        btn2 = types.KeyboardButton("Сгенерировать подъеб")
        btn3 = types.KeyboardButton("Высрать подъеб для всех")
        markup.add( btn1, btn2, btn3)
        a = randint(0, (update_bd_len() - 1))
        print("Рандомный высер №", a)
        meme = update_bd()
        bot.send_message(message.chat.id, text=meme[a], reply_markup=markup)

    elif message.text == "Высрать подъеб для всех":
        sent = bot.send_message(message.chat.id, text="Ну давай, пиши чо ты хочешь: ")
        bot.register_next_step_handler(sent, register_podieb)


    @bot.callback_query_handler(func = lambda callback: True)
    def callback_message(callback):
        if callback.data == 'add_user':
             bot.send_message(message.chat.id, text="Сейчас нужно заполнить маленькую анкету нового бездаря")
             name = bot.send_message(message.chat.id, text="Введите имя бездаря: ")
             bot.register_next_step_handler(name, name_handler)

    def name_handler(name):
        name = name.text
        tg = bot.send_message(message.chat.id, text=f"Отлично! {name} уже почти в реестре бездарей! Введите ссылку на телеграмм бездаря: ")
        bot.register_next_step_handler(tg, tg_handler, name)

    def tg_handler(tg, name):
        tg = tg.text
        bot.send_message(message.chat.id, text="Поздравляю! В рядах бездарей поплнение, теперь иди и высри ему что нибудь!")
        check_tg(name, tg)

    def check_tg(name, tg):
        if tg[0] == "@":
            tg_link = f"https://t.me/{tg[1: ]}"
            register_user(name, tg_link)
        elif tg[0:12] != "https://t.me/":
            tg_link = f"https://t.me/{tg[0: ]}"
            register_user(name, tg_link)
        else:
            register_user(name, tg)


def register_user(newuser_name, newuser_tg):
    con = sqlite3.connect("users.sqlite3", check_same_thread=False)
    cur = con.cursor()
    cur.execute('''INSERT INTO users (Name, tg) VALUES (?, ?)''', (str(newuser_name), str(newuser_tg)))
    con.commit()
    update_bd()



def update_bd_len():
    con = sqlite3.connect("data.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM meme")
    meme = cursor.fetchall()
    memelen = meme.__len__()
    print("Данные бд обновлены! Количество данных - ", memelen - 1)
    return memelen

def update_bd():
    con = sqlite3.connect("data.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM meme")
    meme = cursor.fetchall()
    return(meme)

def register_podieb(message):
    def congrats_m():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        print(meme.__len__())
        btn1 = types.KeyboardButton("Выбрать бездаря")
        btn2 = types.KeyboardButton("Сгенерировать подъеб")
        btn3 = types.KeyboardButton("Высрать подъеб для всех")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Поздравляю, ты поделился своим высером! Он успешно зафикисирован и будет показываться другим пользователям.",
                         reply_markup=markup)
    print(meme.__len__())
    podieb = message.text
    add_bd(podieb)
    congrats_m()



bot.infinity_polling()
