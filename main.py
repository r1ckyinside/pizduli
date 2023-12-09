import telebot
import sqlite3
from telebot import types
from importfromdata import meme
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
        item1 = types.InlineKeyboardButton(text="Рики", url='https://t.me/rickyinside')
        item2 = types.InlineKeyboardButton(text="Влада", url='https://t.me/ove4ka_b')
        item3 = types.InlineKeyboardButton(text="Тёма", url='https://t.me/fl0kse')
        item4 = types.InlineKeyboardButton(text="Даша", url='https://t.me/he_hentaii')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.from_user.id, "Выбери кому дать пизды", reply_markup=markup)

    elif message.text == "Сгенерировать подъеб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выбрать бездаря")
        btn2 = types.KeyboardButton("Сгенерировать подъеб")
        btn3 = types.KeyboardButton("Высрать подъеб для всех")
        markup.add(btn1, btn2, btn3)
        a = randint(0, (update_bd_len() - 1))
        print(a)
        meme = update_bd()
        print(meme)
        bot.send_message(message.chat.id, text=meme[a], reply_markup=markup)

    elif message.text == "Высрать подъеб для всех":
        sent = bot.send_message(message.chat.id, text="Ну давай, пиши чо ты хочешь: ")
        bot.register_next_step_handler(sent, register_podieb)


def update_bd_len():
    con = sqlite3.connect("data.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM meme")
    meme = cursor.fetchall()
    memelen = meme.__len__()
    print("Данные бд обновлены! ", memelen - 1)
    return memelen

def update_bd():
    con = sqlite3.connect("data.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM meme")
    meme = cursor.fetchall()
    print(meme)
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
