from telegram import Update
from telegram.ext import Updater, CommandHandler
from services.chat.TelegramApiInterface import TelegramApiInterface


class TelegramApiService(TelegramApiInterface):
    def __init__(self, api_key, webhook_url):
        self.updater = Updater(token=api_key, use_context=True)
        self.updater.bot.setWebhook(webhook_url)

    def add_command(self, name, implementation):
        self.updater.dispatcher.add_handler(CommandHandler(name, implementation))

    def process_update(self, update):
        self.updater.dispatcher.process_update(Update.de_json(update, self.updater.bot))
