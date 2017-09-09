#!/usr/bin/python3 

import datetime

import ephem

import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler


PLANET=0


def greet_user(bot, update):
    text='Hello, {} {}'.format(update.message.chat.first_name,update.message.chat.last_name )
    print(text)
    print(update)
    update.message.reply_text(text)


def talk_to_me(bot,update):
    usertext=update.message.text 
    print(usertext)
    update.message.reply_text(usertext)


def getconstellation(bot,update,planets):
    todaydate=datetime.date.today().isoformat() 
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
    #planets=update.message.text.split()
    if len(planets)>0 :
        hello_text='Hello, {} {}.'.format(update.message.chat.first_name,update.message.chat.last_name)
        text=''
        for planet in planets :
            planetC=planet.capitalize()
            if planetC in solar:
                planetephem=solar[planetC]
                planet_constellation=ephem.constellation(planetephem)
                #print(planet_constellation)
                planet_text='You chose planet {}\n{} is in {} today'.format(planetC,planetC,planet_constellation[1])

            elif planet=='Earth' :
                planet_text='You are already on Earth'
            else:
                planet_text='I don\'t know planet {}'.format(planet)
            text=text+'\n\n'+planet_text
        text=hello_text+'\n'+text
    else: 
        text='Hello, {} {}.\nEnter any planet as: /planet planet'.format(update.message.chat.first_name,update.message.chat.last_name)
    #print(update)
    update.message.reply_text(text)


def planet_conv(bot,update):
    update.message.reply_text('Hi! Enter you planet')
    return PLANET 


def cancel(bot,update):
    update.message.reply_text('Bye!')
    return ConversationHandler.END


def getplanet(bot,update,args): 
    getplanets=args 
    getconstellation(bot,update,getplanets)
  

def getplanet2(bot,update):
    getplanets=update.message.text.split() 
    getconstellation(bot,update,getplanets)
    update.message.reply_text('Enter any planet')
    return PLANET 


def wordcount(bot,update,args): 
    words=len(args)
    update.message.reply_text('{} words'.format(words))
    


def main():
    updater=Updater(settings.TELEGRAM_BOT_KEY)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", getplanet,pass_args=True))
    dp.add_handler(CommandHandler("wordcount", wordcount,pass_args=True))
    dp.add_handler(ConversationHandler( 
        entry_points=[CommandHandler('planet_conv', planet_conv)],
        states={
#                PLANET: [RegexHandler('^(Mercury|Venus|Mars|Jupiter|Saturn|Uranus|Neptune|Pluto)$',getplanet2)]
                 PLANET: [MessageHandler(Filters.text,getplanet2)]
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        ))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
