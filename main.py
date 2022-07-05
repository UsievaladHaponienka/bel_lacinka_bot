from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater

import config
import Coverter


def help(update, context):
    update.message.reply_text('/help')


def start(update, context):
    update.message.reply_text(
        'Прывітанне! Я - БелЛацінкаБот. Напішыце мне што-небудзь беларускай кірілыцай - '
        'а я канвертую Ваш тэкст на лацінку. Я яшчэ малады і магу рабіць памылкі (як і ўсе мы ў працэсе вывучэння '
        'роднай мовы), таму не судзіце занадта строга)\n\n'
        'Pryvitannie! Ja - BielLacinkaBot. Napišycie mnie što-niebudź bielaruskaj kirilycaj - '
        'a ja kanviertuju Vaš tekst na lacinku. Ja jašče malady i mahu rabić pamylki (jak i ǔsie my ǔ pracesie'
        ' vyvučennia rodnaj movy), tamu nie sudzicie zanadta stroha)')


def convert(update, context):
    result = Coverter.convert(update.message.text)
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
