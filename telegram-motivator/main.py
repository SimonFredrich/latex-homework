from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import random

def start(update, context):
    update.message.reply_text('start command received')

def help(update, context):
    update.message.reply_text('help command received')

def error(update, context):
    update.message.reply_text('an error occured')

def text(update, context):
    print("text entered")

def quote(update, context):
    f = open("quotes.txt")
    quotes = f.readlines()
    update.message.reply_text(quotes[random.randint(0, len(quotes)-1)])

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

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, quote))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
