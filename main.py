from auth import TOKEN
from telegram.ext import Updater, CommandHandler
from commands import start, showPlot
if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("showPlot", showPlot))

    updater.start_polling()
    updater.idle()
    print(TOKEN)