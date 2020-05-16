from auth import TOKEN
from telegram.ext import Updater, CommandHandler
from commands import start, showPlot
from processing.start_scrapper import star_scrapper as str_sc



if __name__ == '__main__':
    # st = str_sc()
    # print(st.stars_list)
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("showPlot", showPlot))

    updater.start_polling()
    updater.idle()
