from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import random
import urllib.request
from lxml import html
from bs4 import BeautifulSoup
import time


def wikipedia_news(update, context):
    update.message.reply_text("Wikipedia news have been initiated!")
    while True:
        time.sleep(60)
        timestamp = time.strftime('%H%M')
        if (timestamp == "0700"):
            url = "https://de.wikipedia.org/wiki/Wikipedia:Hauptseite"
            sock = urllib.request.urlopen(url).read().decode("utf-8")
            soup = BeautifulSoup(sock, 'html.parser')

            news = soup.find(id="nachrichten").find_all('ul')[1].find_all('li')
            for n in news:
                update.message.reply_text(n.text)

def start(update, context):
    update.message.reply_text('start command received')

def help(update, context):
    update.message.reply_text('help command received')

def error(update, context):
    update.message.reply_text('an error occured')

def text(update, context):
    print("text entered")

def main():
    file_variable = open('token.txt')
    lines = file_variable.readlines()
    TOKEN = lines[0]

    # create the updater, that will automatically create also a dispatcher and a queue to 
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("news", wikipedia_news))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
