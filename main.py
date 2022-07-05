from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
import random
import config
import Coverter
import Rules


def start(update, context):
    update.message.reply_text(
        'Прывітанне! Я - БелЛацінкаБот. Напішыце мне што-небудзь беларускай кірілыцай - '
        'а я канвертую Ваш тэкст на лацінку. Я яшчэ малады і магу рабіць памылкі (як і ўсе мы ў працэсе вывучэння '
        'роднай мовы), таму не судзіце занадта строга)\n'
        "Каб даведацца, што я яшчэ магу, акрамя канвертацыі кірыліцы ў лацінку, скарыстайцеся камандай /help\n\n"
        'Pryvitannie! Ja - BielLacinkaBot. Napišycie mnie što-niebudź bielaruskaj kirilycaj - '
        'a ja kanviertuju Vaš tekst na lacinku. Ja jašče malady i mahu rabić pamylki (jak i ǔsie my ǔ pracesie'
        ' vyvučennia rodnaj movy), tamu nie sudzicie zanadta stroha)\n'
        'Kab daviedacca, što ja jašče mahu, akramia kanviertacyi kirylicy ǔ lacinku, skarystajciesia kamandaj /help')


def help(update, context):
    update.message.reply_text(
        '/start - Прывітальнае паведамленне\n'
        '/help - спіс каманд (зараз вы яго і бачыце)\n'
        '/rules + лічба ад 1 да 4 - правіла выкарыстання беларускай лацінка. Так, іх усяго, бо лацінка - гэта, '
        'насамрэч, даволі лёгка)\n'
        '/history - тут пакуль нічога няма, але хутка будуць гістарыныя прыклады выкарыстання лацінкі\n\n'
        '/start - Pryvitaĺnaje paviedamliennie\n'
        '/help - spis kamand (zaraz vy jaho i bačycie)\n'
        '/rules + ličba ad 1 da 4 - pravila vykarystannia bielaruskaj lacinka. Tak, ich usiaho 4, bo lacinka - heta, '
        'nasamreč, davoli liohka)\n'
        '/history - tut pakuĺ ničoha niama, alie chutka buduć histarynyja pryklady vykarystannia lacinki'
    )


def convert(update, context):
    if update.message.text.lower() == 'жыве беларусь!':
        update.message.reply_text("Жыве вечна!")
    result = Coverter.convert(update.message.text)
    update.message.reply_text(result)


def rules(update, context):
    if len(update.message.text.split()) > 1 and int(update.message.text.split()[1]) <= (len(Rules.get_rules()) - 1):
        result = Rules.get_rules()[int(update.message.text.split()[1]) - 1]
    else:
        result = random.choice(Rules.get_rules())

    link = Rules.get_link()
    update.message.reply_text(result + "\n\n" + link)


def history(update, context):
    update.message.reply_text("Тут пакуль нічога няма, але хутка абавязкова будзе!\n\n"
                              "Tut pakuĺ ničoha niama, alie chutka abaviazkova budzie!")


def main():
    updater = Updater(config.getToken(), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("history", history))

    dp.add_handler(MessageHandler(Filters.text, convert))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
