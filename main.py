from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from Coverter import Converter
import config

converter = Converter()

def help(update, context):
    update.message.reply_text('/help')

def start(update, context):
    update.message.reply_text('Hi, dude!')

def convert(update, context):
    result = converter.convert(update.message.text)
    update.message.reply_text(result)

def main():
    updater = Updater(config.getToken(), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, convert))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()