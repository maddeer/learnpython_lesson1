#!/usr/bin/python3 
#u={'update_id': 837881545, 'message': {'new_chat_photo': [], 'entities': [{'length': 7, 'offset': 0, 'type': 'bot_command'}], 'channel_chat_created': False, 'chat': {'last_name': 'Deer', 'id': 431329364, 'first_name': 'Mad', 'type': 'private'}, 'new_chat_members': [], 'from': {'is_bot': False, 'last_name': 'Deer', 'id': 431329364, 'language_code': 'ru-RU', 'first_name': 'Mad'}, 'new_chat_member': None, 'photo': [], 'group_chat_created': False, 'date': 1504779124, 'message_id': 60, 'supergroup_chat_created': False, 'text': '/planet mars', 'delete_chat_photo': False}}

from telegram.ext import Updater, CommandHandler, MessageHandler,Filters 
import settings
import ephem
import datetime

def greet_user(bot, update):
    text='Hello, {} {}'.format(update.message.chat.first_name,update.message.chat.last_name )
    print(text)
    print(update)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    usertext=update.message.text 
    print(usertext)
    update.message.reply_text(usertext)

def getplanet(bot,update,args):
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
    planets=args
    if len(planets)>0 :
        hello_text='Hello, {} {}.'.format(update.message.chat.first_name,update.message.chat.last_name)
        text=''
        planet=planets[0]
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


def main():
    updater=Updater(settings.TELEGRAM_BOT_KEY)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", getplanet,pass_args=True))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
