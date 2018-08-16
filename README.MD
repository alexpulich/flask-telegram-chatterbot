# flask-telegram-chatterbot

Simple flask application for telegram bot with webhooks and chatterbot as ML engine.

## Getting Started

1. Clone repository: `git@github.com:alexpulich/flask-telegram-chatterbot.git`

2. Install all the dependencies: `pip install -r requirements.txt` 

3. Probably you will need [ngrok](https://ngrok.com) to make a tunnel to your localhost, 
so you can run the bot locally. After you get it, run: `/path/to/ngrok http 5000`

4. Create a src/app/credentials.py file using credentials.example.py as an example.
When filling up the URL_ROOT don't forget to save the trailing slash, 
e.g. `URL_ROOT = 'https://9a5eb2fb.ngrok.io/'`

4. Go to source directory: `cd src`

5. Set FLASK_APP env variable: `export FLASK_APP=manage`

6. Run the application: `flask run`

## Built With

* [Flask](http://flask.pocoo.org) - The web framework used
* [Python-telegram-bot](https://python-telegram-bot.org) - Telegram API library
* [Chatterbot](https://chatterbot.readthedocs.io/en/stable/) - ML, conversational dialog engine

## Authors

* **Alex Pulich** - *Currently all the work* - [alexpulich](https://github.com/alexpulich)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/83ca49330e0a43d3a94198e9f7ea96a5)](https://www.codacy.com/project/alexpulich/flask-telegram-chatterbot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexpulich/flask-telegram-chatterbot&amp;utm_campaign=Badge_Grade_Dashboard)