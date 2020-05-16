import matplotlib.pyplot as plt
import io
from PIL import Image
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='as')

def showPlot(update, context):
    plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
    plt.xlabel('Months')
    plt.ylabel('Books Read')
    plt.title("test")
    plt.savefig('figure.png')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open('./figure.png', 'rb'))

