import telebot
import psycopg2
import datetime
from telebot import types
from datetime import date  

bot = telebot.TeleBot('5012602272:AAGxUOvu-YgaEnxTSP3QbBuut9Iez_R5tO8')

conn = psycopg2.connect(database = "rasp",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
cursor = conn.cursor()

@bot.message_handler(commands=['hello'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnChet = types.KeyboardButton('Расписание на неделю')
    btnSev = types.KeyboardButton('Расписание на сегодня')
    btnZav = types.KeyboardButton('Расписание на завтра')
    markup.add(btnChet)
    markup.add(btnSev)
    markup.add(btnZav)
    bot.send_message(message.chat.id, 'Выберите что вам нужно' , reply_markup=markup) 



@bot.message_handler(content_types='text')
def reply_message(message):
    if message.text == 'Расписание на сегодня':
        current_dt= datetime.datetime.today().weekday()        
        result = ['Пн','Вт','Ср','Чт','Пт','Сб','Вск']
        a = result[current_dt]
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day=%s",[str(a)])
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        if result == '':
            result = 'сегодня можно спать!'
        bot.send_message(message.chat.id, result)                                                              
        
    if message.text == 'Расписание на завтра':
        current_dt= datetime.datetime.today().weekday()        
        result = ['Пн','Вт','Ср','Чт','Пт','Сб','Вск']
        a = result[current_dt+1]
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day=%s",[str(a)])
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        if result == '':
            result = 'сегодня можно спать!'
        bot.send_message(message.chat.id, result)    

    if message.text == 'Расписание на неделю':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnPn = types.KeyboardButton('Понедельник')
        btnVt = types.KeyboardButton('Вторник')
        btnSr = types.KeyboardButton('Среда')
        btnCht = types.KeyboardButton('Четверг')
        btnPt = types.KeyboardButton('Пятница')
        btnSb = types.KeyboardButton('Суббота')
        btnVsk = types.KeyboardButton('Воскресенье')
        markup.add(btnPn)
        markup.add(btnVt)  
        markup.add(btnSr)
        markup.add(btnCht)
        markup.add(btnPt)  
        markup.add(btnSb)
        markup.add(btnVsk)         
        bot.send_message(message.chat.id, 'Выберите дату по которой вы хотите узнать какие будут пары' , reply_markup=markup)
    if message.text == 'Понедельник':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пн'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Вторник':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Вт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)
        
    if message.text == 'Среда':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Ср' ")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Четверг':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Чт'  ")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Пятница':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Суббота':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Сб'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Воскресенье':
        bot.send_message(message.chat.id, 'Можно спать весь день!')






bot.infinity_polling()