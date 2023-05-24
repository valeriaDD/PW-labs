from telegram.ext import Updater, CommandHandler
from chat.TelegramApiProvider import TelegramApiProvider


class TelegramApiAdapter(TelegramApiProvider):
    def __init__(self, api_key):
        self.updater = Updater(token=api_key, use_context=True)

    def add_command(self, name, implementation):
        self.updater.dispatcher.add_handler(CommandHandler(name, implementation))

    def start(self):
        self.updater.start_polling()
