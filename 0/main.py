from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
from collections import defaultdict
import time
from time import *
import random
from datetime import datetime
import os
 
app = Client("my_account")
chat = "pyrogramlounge"
limit = 2000

people = []
class custom(dict):
    def __missing__(self, key):
        return 0

class custom(dict):
    def __missing__(self, key):
        return 0

ALL_MESSAGES = defaultdict(list)
# Команда type


REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "#"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 
# Команда взлома пентагона
@app.on_message(filters.command("tef", prefixes=".") & filters.me)
def tef(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об Tefal ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об Tefal ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании мулитиварок Tefal на земле!")
 
@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
@app.on_message(filters.command("p", prefixes=".    ") & filters.me)
def p(_, msg):
    user = "me"
    all_pics = app.iter_profile_photos(user)
    for i, pic in enumerate(all_pics, 1):
        path = app.download_media(
            message=pic.file_id,
            file_ref=pic.file_ref,
            file_name=f"profile_pics/{user}/{i}.jpg",
        )
        print(path.split("\\")[-1]) 


@app.on_message(filters.command("count", prefixes=".") & filters.me)
def count(_, msg):
    for member in app.iter_chat_members(target):
        print(member.user.first_name)

@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)

@app.on_message(filters.command("who", prefixes=".") & filters.me)
def join_date(_, msg):

    members = []

    for m in app.iter_chat_members(msg.chat.id):
        members.append(
            (

                m.user.first_name,
                m.joined_date or app.meget_ssages(msg.chat.id, 1).date,

            )
        )


    members.sort(key=lambda member: member[1])

    with open("joined_date_members.txt", "w", encoding="utf8") as f:
        f.write("Дата входа(в группу)      Имя\n")
        for member in members:
            f.write(
                str(datetime.fromtimestamp(member[1]).strftime("%y-%m-%d %H:%M"))
                + f" {member[0]}\n"

            )
          
         

    app.send_document(msg.chat.id, "joined_date_members.txt")
    msg.edit("🛠 Участники сохранены 🛠")
    os.remove("joined_date_members.txt")

@app.on_message(filters.command("lest", prefixes=".") & filters.me)
def lastMessage(_, msg):
    members = []
     for m in app.iter_chat_members(msg.chat.id):

        if member.user.is_deleted:
            continue
        x = member.user.first_name
        y = member.user.first_name.encode().decode("ascii", "ignore")
        if x != y:
            members.append(
                (
                member.user.first_name,
                member.user.first_name.encode().decode("ascii", "ignore")
                )
            )
    members.sort(key=lambda member: member[1])
    with open("notStandartNick.txt", "w", encoding="utf8") as f:
        f.write("Ник        Ник без символов(юникод)\n")
        for member in members:
            f.write(
                str(datetime.fromtimestamp(member[1]).strftime("%y-%m-%d %H:%M"))
                + f" {member[0]}\n"

            )
    app.send_document(msg.chat.id, "notStandartNick.txt")
    msg.edit("🛠 Ники сохранены 🛠")
    os.remove("notStandartNick.txt")

app.run()