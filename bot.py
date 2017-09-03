#!/usr/bin/python3 

from telegram.ext import Updater, CommandHandler, MessageHandler,Filters 
import settings

def greet_user(bot, update):
    text='Hello, {} {}'.format(update.message.chat.first_name,update.message.chat.last_name )
    print(text)
    print(update)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    usertext=update.message.text 
    print(usertext)
    update.message.reply_text(usertext)

def main():
    updater=Updater(settings.TELEGRAM_BOT_KEY)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
