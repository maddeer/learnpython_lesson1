#!/usr/bin/python3 

import datetime
import logging

import ephem

import settings

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler


PLANET = 0
NUMBER, CALC = range(2)


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
            filename='bot.log'
)



def greet_user(bot, update):
    text = 'Hello, {} {}'.format(update.message.chat.first_name,update.message.chat.last_name )
    print(text)
    print(update)
    update.message.reply_text(text)


def talk_to_me(bot,update):
    usertext = update.message.text 
    print(usertext)
    update.message.reply_text(usertext)


def getconstellation(bot,update,planets):
    todaydate = datetime.date.today().isoformat() 
    solar={
            'Mercury': ephem.Mercury(todaydate),
            'Venus':   ephem.Venus(todaydate),
            'Mars':    ephem.Mars(todaydate),
            'Jupiter': ephem.Jupiter(todaydate),
            'Saturn':  ephem.Saturn(todaydate),
            'Uranus':  ephem.Uranus(todaydate),
            'Neptune': ephem.Neptune(todaydate),
            'Pluto':   ephem.Pluto(todaydate)
            }
    #planets = update.message.text.split()
    if not planets:
        text = 'Hello, {} {}.\nEnter any planet as: /planet planet'.format(update.message.chat.first_name, update.message.chat.last_name)
        return 

    hello_text = 'Hello, {} {}.'.format(update.message.chat.first_name, update.message.chat.last_name)
    text = ''
    for raw_planet in planets :
        planet_name = raw_planet.capitalize()
        if planet_name in solar:
            planet_ephem = solar[planet_name]
            planet_constellation = ephem.constellation(planet_ephem)
            #print(planet_constellation)
            planet_text = 'You chose planet {}\n{} is in {} today'.format(planet_name, planet_name, planet_constellation[1])

        elif planet=='Earth' :
            planet_text = 'You are already on Earth'
        else:
            planet_text = 'I don\'t know planet {}'.format(planet)
        text = text+'\n\n'+planet_text
    text = hello_text+'\n'+text
    update.message.reply_text(text)


def planet_conv(bot,update):
    update.message.reply_text('Hi! Enter you planet')
    return PLANET 


def cancel(bot,update):
    update.message.reply_text('Bye!')
    return ConversationHandler.END


def getplanet(bot,update,args): 
    getplanets = args 
    getconstellation(bot,update,getplanets)
  

def getplanet2(bot,update):
    getplanets = update.message.text.split() 
    getconstellation(bot,update,getplanets)
    update.message.reply_text('Enter any planet')
    return PLANET 


def wordcount(bot,update): 
    text=update.message.text.split('"')
    words=0
    if len(text)>1:
        words = len(text[1].split())
    update.message.reply_text('{} words'.format(words))
    

def calculator(bot, update, args):
    getmath = ''.join(args).strip('=')
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
            if math_list[1].strip() != '0' :
                result_math = float(math_list[0].strip()) / float(math_list[1].strip())
            else: 
                update.message.reply_text('can\'t count zerro')
        else:
            update.message.reply_text('not a mathematic')
            return 
    except (TypeError,ValueError):
            update.message.reply_text('not a mathematic')
            return 
    update.message.reply_text('result {}'.format(result_math))

def calculator2(bot,update):
    custom_keyboard = [ ['1', '2', '3', '*'],
                        ['4', '5', '6', '/'],
                        ['7', '8', '9', ],
                        ['0', '+', '-', '=']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text('Enter the leter', reply_markup=reply_markup)
    return NUMBER


def getbutton(bot,update):
    global NUMBERS_TEXT
    if update.message.text == '=' : 
        calculator(bot,update,NUMBERS_TEXT)
        update.message.reply_text('BYE!',reply_markup=ReplyKeyboardRemove())
        NUMBERS_TEXT=''
        return ConversationHandler.END
    else:
        text_enterd = update.message.text
        NUMBERS_TEXT+=text_enterd 
        update.message.reply_text('You pressed {}. Enter another leter'.format(NUMBERS_TEXT))
    return NUMBER 


def main():
    updater = Updater(settings.TELEGRAM_BOT_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", getplanet, pass_args = True))
    dp.add_handler(CommandHandler("wordcount", wordcount) ) #, pass_args = True))
    dp.add_handler(CommandHandler("calculator", calculator, pass_args = True))
    dp.add_handler(ConversationHandler( 
        entry_points = [CommandHandler('planet_conv', planet_conv)],
        states={
#                planet: [regexhandler('^(mercury|venus|mars|jupiter|saturn|uranus|neptune|pluto)$',getplanet2)]
                 PLANET: [MessageHandler(Filters.text, getplanet2)]
            },
        fallbacks = [CommandHandler('cancel', cancel)]
        ))
    dp.add_handler(ConversationHandler( 
        entry_points = [CommandHandler('calculator2', calculator2)],
        states={
                 NUMBER: [MessageHandler(Filters.text, getbutton)],
            },
        fallbacks = [CommandHandler('cancel', cancel)]
        ))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()


NUMBERS_TEXT = '' 
if __name__ == '__main__':
    main()
