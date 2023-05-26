from flask import Flask, request

import config
from services.chat.TelegramApiService import TelegramApiService
from database.DatabaseManager import DatabaseManager
from services.news.NewsApiAdapter import NewsApiAdapter

app = Flask(__name__)


def start_command_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Wanna read some news?")


def list_command_handler(update, context):
    user_says = " ".join(context.args) if len(context.args) > 0 else None
    try:
        news = newsAPI.get_news(user_says)
        for new in news:
            context.bot.send_message(chat_id=update.effective_chat.id, text=new)
    except FileNotFoundError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ups, records not found")


def save_command_handler(update, context):
    if len(context.args) > 0:
        user_says = " ".join(context.args)
        database.save_data(update.effective_chat.id, user_says)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Seems like you didn't provide any data to save, please complete the command"
        )



def show_command_handler(update, context):
    result = database.get_saved_data(update.effective_chat.id)

    if result != "":
        text = "Here are your saved data:\r\n" + result
    else:
        text = "You dont have any saved data yet"

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)




@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json(force=True)
    telegramAPI.process_update(update)
    return 'OK'


if __name__ == "__main__":
    database = DatabaseManager()
    newsAPI = NewsApiAdapter(config.tokens['NEWS'])
    telegramAPI = TelegramApiService(config.tokens['TELEGRAM'], config.ngrok)

    telegramAPI.add_command('start', start_command_handler)
    telegramAPI.add_command('latest_news', list_command_handler)
    telegramAPI.add_command('save_news', save_command_handler)
    telegramAPI.add_command('saved_news', show_command_handler)

    app.run()
