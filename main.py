import telebot
import sqlite3
from telebot import types
from importfromdata import meme
from random import randint

bot = telebot.TeleBot("6957840347:AAHwUYKl59mWjqOBheue5IMj_CsFxU3pykc")
con = sqlite3.connect("data.sqlite3", check_same_thread=False)
cur = con.cursor()


def add_bd(usermeme):
    cur.execute('''INSERT INTO meme (?)''', usermeme)
    con.commit()


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
        bot.send_message(message.chat.id, text=meme[randint(0, 11)], reply_markup=markup)

    elif message.text == "Высрать подъеб для всех":
        bot.send_message(message.chat.id, text="Ну давай, пиши чо ты хочешь: ")
        meme_by_user = message.text
        add_bd(meme_by_user)


bot.infinity_polling()
