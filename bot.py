#!/usr/bin/python3 

from telegram.ext import Updater, CommandHandler, MessageHandler,Filters 
def greet_user(bot, update):
    text='Вызван /start'
    print(text)
    print(update)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    usertext=update.message.text 
    print(usertext)
    update.message.reply_text(usertext)

def main():
    updater=Updater("361739349:AAG8GSv9k0KxuN3urYsw5Sx6Rw6x3tu1qcI")
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    updater.start_polling()
    updater.idle()
main()
