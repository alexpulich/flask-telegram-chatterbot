"""
Bot module
"""
from chatterbot import ChatBot


class Bot:
    """
    Represents bot
    """
    def __init__(self, name, database_file, default_response):
        """
        Initialize a bot instance for project
        :param name: chatbot's name
        :param database_file: path to sqlite database file
        :param default_response: response to send when can't find out the answer in
        """
        self.bot = self._create_chatbot(name, database_file, default_response)

    def get_response(self, message):
        """
        Get response from chatterbot for user's message
        :param str message: message to answer
        :return: answer
        :rtype: str
        """
        statement = self.bot.get_response(message)
        response = statement.text
        return response

    def _create_chatbot(self, name, database_file, default_response):
        """
        Create chatterbot.ChatBot instance
        :param str name: chatbot's name
        :param str database_file: path to sqlite database file
        :param str default_response: response to send when can't find out the answer in
        :return: ChatBot instance
        :rtype: chatterbot.ChatBot
        """
        chatbot = ChatBot(
            name,
            database=database_file,
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'response_selection_method': 'chatterbot.response_selection.get_most_frequent_response'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.60,
                    'default_response': default_response
                }
            ],
            filters=[
                'chatterbot.filters.RepetitiveResponseFilter'
            ]
        )

        return chatbot
