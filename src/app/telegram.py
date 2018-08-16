from flask import current_app

import telegram
from telegram.ext import Dispatcher, Filters, MessageHandler

from queue import Queue

TELEGRAM_API_KEY = 'TELEGRAM_API_KEY'


class TelegramBotManager:
    """
    Manager for telegram bot
    """

    def __init__(self, token):
        """
        Initialize a manager for telegram bot
        :param str token: Telegram API Key
        """
        self.token = token
        self.bot = telegram.Bot(token)
        self.name = self.bot.name
        self.update_queue = Queue()
        self.dispatcher = Dispatcher(self.bot, self.update_queue)

    def set_webhook(self):
        """
        Setting webhook for telegram bot
        :return:
        """
        try:
            webhook_url = '{}tg'.format(current_app.config['URL_ROOT'],)

            if webhook_url != self.bot.getWebhookInfo()['url']:
                self.bot.setWebhook(webhook_url)

        except telegram.error.NetworkError as e:
            # Todo logging
            pass
            # app.logger.error(e.args)

    def init_handlers(self):
        """
        Initializing handlers for different types of messages
        :return:
        """
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.text_handler))

    def handle_request(self, data):
        """
        Handles every request from telegram invoking dispatcher
        :param data:
        :return: just ok in any case. Seems like need to edit
        :rtype: str
        """
        update = telegram.Update.de_json(data, self.bot)
        self.dispatcher.process_update(update)
        return 'ok'

    def init(self):
        """
        Doing some initializing stuff for instance like setting webhooks, etc
        :return:
        """
        self.set_webhook()
        self.init_handlers()

    @staticmethod
    def text_handler(bot, update):
        """
        Handler for text messages from telegram
        :param telegram.Bot bot: telegram bot instance
        :param telegram.Update update: telegram update instance
        :return:
        """
        message = update.message

        message_text = message.text
        chat_id = message.chat.id
        response = current_app.bot.get_response(message_text)

        bot.send_message(chat_id=chat_id, text=response)