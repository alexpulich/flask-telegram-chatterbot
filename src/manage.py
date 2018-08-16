"""
Entry point for application
Provides Flask app created using fabric and cli for chatbot's training
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

import click

from pathlib import Path

from app import create_app

app = create_app()


@app.cli.command()
@click.option('--corpus')
@click.option('--file')
def train(corpus, file):
    """
    Training chatbot using chatterbot_corpus corpuses or txt file
    :param str corpus: language from chatterbot_corpus, e.g.: russian, english
    :param str file: path to txt file with dialogs to train on
    :return:
    """
    if corpus:
        corpus = corpus.strip().lower()
        chatbot = ChatBot(
            database=app.config['DATABASE_FILE'],
            name=app.config['BOT_NAME']
        )
        chatbot.set_trainer(ChatterBotCorpusTrainer)
        try:
            chatbot.train(f'chatterbot.corpus.{corpus}')
        except FileNotFoundError:
            print('Please, use a language name as a value for --corpus option, e.g.: russian, english, etc')

    if file:
        my_file = Path(file)
        if not my_file.is_file():
            print(f'{file} does not exist. Please, specify existing one!')
            return

        dialogs = get_dialogs_from_file(file)

        if dialogs:
            chatbot = ChatBot(
                database=app.config['DATABASE_FILE'],
                name=app.config['BOT_NAME']
            )
            chatbot.set_trainer(ListTrainer)
            for dialog in dialogs:
                chatbot.train(dialog)


def get_dialogs_from_file(file):
    """
    Reads file and returns list of lists with dialogs
    Each inner list is a separate dialog
    Each item in each inner list is a phrase
    :param str file: path to txt file with dialogs to train on
    :return: dialogs to train on
    :rtype: dict
    """
    dialogs = []
    with open(file) as file:
        tmp_dialog = []
        for line in file:
            strip_line = line.strip()
            if strip_line:
                tmp_dialog.append(strip_line)
            else:
                dialogs.append(tmp_dialog[:])
                tmp_dialog = []
    if tmp_dialog:
        dialogs.append(tmp_dialog[:])
    return dialogs


if __name__ == '__main__':
    app.run(debug=True)
