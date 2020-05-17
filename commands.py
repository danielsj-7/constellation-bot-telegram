import matplotlib.pyplot as plt

from processing.start_scrapper import star_scrapper as str_sc

st = str_sc()
dot_map = st.create_dot_map()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='as')


def showPlot(update, context):
    x = dot_map[0]
    y = dot_map[1]
    ax = plt.gca()
    ax.scatter(x, y, s=1.0, c="black", )
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.scatter(x, y)
    plt.axis('off')
    plt.savefig('figure.png')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open('./figure.png', 'rb'))

