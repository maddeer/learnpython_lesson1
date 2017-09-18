#!/usr/bin/env python3

import datetime
import logging
import re

import ephem

import settings

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler


PLANET = 0
NUMBER, CALC = range(2)

CITY = []

NUMBERS_TEXT = ''

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(bot, update):
    text = 'Hello, {} {}'.format(update.message.chat.first_name, update.message.chat.last_name)
    print(text)
    print(update)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    usertext = update.message.text
    print(usertext)
    update.message.reply_text(usertext)


def getconstellation(bot, update, planets):
    todaydate = datetime.date.today().isoformat()
    solar = {
            'Mercury': ephem.Mercury(todaydate),
            'Venus':   ephem.Venus(todaydate),
            'Mars':    ephem.Mars(todaydate),
            'Jupiter': ephem.Jupiter(todaydate),
            'Saturn':  ephem.Saturn(todaydate),
            'Uranus':  ephem.Uranus(todaydate),
            'Neptune': ephem.Neptune(todaydate),
            'Pluto':   ephem.Pluto(todaydate)
            }
    # planets = update.message.text.split()
    if not planets:
        text = 'Hello, {} {}.\nEnter any planet as: /planet planet'.format(update.message.chat.first_name, update.message.chat.last_name)
    return
    hello_text = 'Hello, {} {}.'.format(update.message.chat.first_name, update.message.chat.last_name)
    text = ''
    for raw_planet in planets:
        planet_name = raw_planet.capitalize()
        if planet_name in solar:
            planet_ephem = solar[planet_name]
            planet_constellation = ephem.constellation(planet_ephem)
            # print(planet_constellation)
            planet_text = 'You chose planet {}\n{} is in {} today'.format(planet_name, planet_name, planet_constellation[1])

        elif planet == 'Earth':
            planet_text = 'You are already on Earth'
        else:
            planet_text = 'I don\'t know planet {}'.format(planet)
        text = text+'\n\n'+planet_text
    text = hello_text+'\n'+text
    update.message.reply_text(text)


def planet_conv(bot, update):
    update.message.reply_text('Hi! Enter you planet')
    return PLANET


def cancel(bot, update):
    update.message.reply_text('Bye!')
    return ConversationHandler.END


def getplanet(bot, update, args):
    getplanets = args
    getconstellation(bot, update, getplanets)


def getplanet2(bot, update):
    getplanets = update.message.text.split()
    getconstellation(bot, update, getplanets)
    update.message.reply_text('Enter any planet')
    return PLANET


def wordcount(bot, update):
    text_list = re.findall('\"([^"]*)\"',update.message.text)
    words = 0
    for text_item in text_list:
        words += len(text_item.split())
    update.message.reply_text('{} words'.format(words))


def calculator(bot, update, args):
    getmath = ''.join(args).replace(' ','').strip('=')
    try:
        if '-' in getmath:
            math_list = getmath.split('-')
            result_math = float(math_list[0].strip()) - float(math_list[1].strip())
        elif '+' in getmath:
            math_list = getmath.split('+')
            result_math = float(math_list[0].strip()) + float(math_list[1].strip())
        elif '*' in getmath:
            math_list = getmath.split('*')
            result_math = float(math_list[0].strip()) * float(math_list[1].strip())
        elif '/' in getmath:
            math_list = getmath.split('/')
            if math_list[1].strip() != '0':
                result_math = float(math_list[0].strip()) / float(math_list[1].strip())
            else:
                update.message.reply_text('can\'t count zerro')
        else:
            update.message.reply_text('not a mathematic')
            return
    except (TypeError, ValueError):
            update.message.reply_text('not a mathematic')
            return
    update.message.reply_text('result {}'.format(result_math))


def calculator2(bot, update):
    custom_keyboard = [['1', '2', '3', '*'],
                       ['4', '5', '6', '/'],
                       ['7', '8', '9', ],
                       ['0', '+', '-', '=']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text('Enter the leter', reply_markup=reply_markup)
    return NUMBER


def getbutton(bot, update):
    global NUMBERS_TEXT
    if update.message.text == '=':
        calculator(bot, update, NUMBERS_TEXT)
        update.message.reply_text('BYE!', reply_markup=ReplyKeyboardRemove())
        NUMBERS_TEXT = ''
        return ConversationHandler.END
    else:
        text_enterd = update.message.text
        NUMBERS_TEXT += text_enterd
        update.message.reply_text('You pressed {}. Enter another leter'.format(NUMBERS_TEXT))
    return NUMBER


def textcalculator(bot, update, args):
    regex_dict = {
                'сколько будет': '=',
                'один': '1',
                'два': '2',
                'три' : '3',
                'четыре': '4',
                'пять': '5',
                'шесть': '6',
                'семь': '7',
                'восемь': '8',
                'девять': '9',
                'ноль': '0',
                'плюс': '+',
                'минус': '-',
                'умножить на': '*',
                'разделить на': '/',
                }
    getformula = ' '.join(args).lower()
    for regex in regex_dict:
        getformula = getformula.replace(regex,regex_dict[regex])

    calculator(bot, update, getformula)

def getfullmoon(bot, update, args):
    get_question=' '.join(args).lower()
    if 'когда ближайшее полнолуние после' in get_question: 
        full_moon_predate=re.findall('([0-9]{4}-[0-9]{2}-[0-9]{2})',get_question)
        if full_moon_predate: 
            for full_moon_date in full_moon_predate: 
                full_moon_date.replace('-','/')
                update.message.reply_text('Полнолуне начнется {}'.format(ephem.next_full_moon(full_moon_date)))
        else:
            update.message.reply_text('задайте вопрос в фотмате:\n'
                '/getfullmoon когда ближайшее полнолуние после ГГГГ-ММ-ДД') 
    else: 
        update.message.reply_text('задайте вопрос в фотмате:\n'
            '/getfullmoon когда ближайшее полнолуние после ГГГГ-ММ-ДД') 


def goroda(bot, update, args):
    if not args: 
        update.message.reply_text('Укажите город')
        return 

    gorod = args[0]
    if not args[0].capitalize() in CITY:
        update.message.reply_text('Такой город уже был или его нет')
        return

    find = False
    for city in CITY:
        if gorod[-1].lower() == 'ъ' or gorod[-1].lower() == 'ь': 
            last = gorod[-2].lower()
        else: 
            last = gorod[-1].lower()  
        
        if city[0].lower() == last:
            update.message.reply_text(city)
            CITY.remove(city)
            CITY.remove(gorod.capitalize())
            find = True
            break 
    if not find: 
        update.message.reply_text('У меня кончились города. Начинаю сначала')
        get_city_list()


def get_city_list():
    with open('cities.txt', 'r', encoding='utf-8') as f: 
        for line in f:
            CITY.append(line.replace('\n','').capitalize())


def main():
    get_city_list()
    updater = Updater(settings.TELEGRAM_BOT_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", getplanet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("calculator", calculator, pass_args=True))
    dp.add_handler(CommandHandler("textcalculator", textcalculator, pass_args=True))
    dp.add_handler(CommandHandler("getfullmoon", getfullmoon, pass_args=True))
    dp.add_handler(CommandHandler("goroda", goroda, pass_args=True))
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('planet_conv', planet_conv)],
        states={
                 PLANET: [MessageHandler(Filters.text, getplanet2)]
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        ))
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('calculator2', calculator2)],
        states={
                 NUMBER: [MessageHandler(Filters.text, getbutton)],
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        ))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
