from flask import Flask

from chat.TelegramApiAdapter import TelegramApiAdapter
from database.DatabaseManager import DatabaseManager
from news.NewsApiAdapter import NewsApiAdapter

app = Flask(__name__)


def start_command_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Wanna read some news?")


def list_command_handler(update, context):
    user_says = " ".join(context.args) if len(context.args) > 0 else None
    news = newsAPI.get_news(user_says)

    for new in news:
        context.bot.send_message(chat_id=update.effective_chat.id, text=new)


def save_command_handler(update, context):
    if len(context.args) > 0:
        user_says = " ".join(context.args)
        database.save_data(update.effective_chat.id, user_says)


def show_command_handler(update, context):
    result = database.get_saved_data(update.effective_chat.id)

    if result != "":
        text = "Here are your saved data:\r\n" + result
    else:
        text = "You dont have any saved data yet"

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


if __name__ == "__main__":
    database = DatabaseManager()
    newsAPI = NewsApiAdapter("fc9232e093cb4d278cdeca26cd049a5f")
    telegramAPI = TelegramApiAdapter('5857957671:AAF4O8AjoU1AGNqZ2DUUTknT-1CwTdRNFVw')

    telegramAPI.add_command('start', start_command_handler)
    telegramAPI.add_command('list', list_command_handler)
    telegramAPI.add_command('save', save_command_handler)
    telegramAPI.add_command('show', show_command_handler)

    telegramAPI.start()
    app.run()
