from flask import Flask
from NewsAPI import NewsAPI
from telegram.ext import Updater, CommandHandler
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    news_token = os.environ.get('NEWS_API_TOKEN')
    newsAPI = NewsAPI(news_token)

    return newsAPI.get_news('test')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Wanna read some news?")


def list(update, context):
    if len(context.args) > 0:
        user_says = " ".join(context.args)
        print(user_says)

    news_token = os.environ.get('NEWS_API_TOKEN')
    newsAPI = NewsAPI(news_token)

    news = newsAPI.get_news('test')

    for new in news:
        context.bot.send_message(chat_id=update.effective_chat.id, text=new)


if __name__ == "__main__":
    token = '5857957671:AAF4O8AjoU1AGNqZ2DUUTknT-1CwTdRNFVw'
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('list', list))

    updater.start_polling()

    app.run()
