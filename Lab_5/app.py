from flask import Flask
from news.NewsApiAdapter import NewsApiAdapter
from telegram.ext import Updater, CommandHandler
import os

app = Flask(__name__)
db = []

newsAPI = NewsApiAdapter("fc9232e093cb4d278cdeca26cd049a5f")


@app.route("/")
def hello_world():
    news_token = os.environ.get('NEWS_API_TOKEN')
    newsAPI = NewsApiAdapter(news_token)

    return newsAPI.get_news('test')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Wanna read some news?")


def list(update, context):
    user_says = None

    if len(context.args) > 0:
        user_says = " ".join(context.args)

    news = newsAPI.get_news(user_says)

    for new in news:
        context.bot.send_message(chat_id=update.effective_chat.id, text=new)


def save(update, context):
    if len(context.args) > 0:
        user_says = " ".join(context.args)
        db.append({'id': update.effective_chat.id, 'data': user_says})


def show(update, context):
    result = ""
    for data in db:
        if data["id"] == update.effective_chat.id:
            result += "\r\n" + data["data"]

    text = "Here are your saved news:\r\n" + result
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


if __name__ == "__main__":
    token = '5857957671:AAF4O8AjoU1AGNqZ2DUUTknT-1CwTdRNFVw'
    # token = os.environ.get("TELEGRAM_BOT_TOKEN")

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('list', list))
    dispatcher.add_handler(CommandHandler('save', save))
    dispatcher.add_handler(CommandHandler('show', show))

    updater.start_polling()
    app.run()

