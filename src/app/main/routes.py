"""
Routes for application's main blueprint
"""

from flask import request, jsonify, current_app
from app.main import bp


@bp.route('/tg', methods=['POST'])
def telegram_webhook():
    """
    Telegram webhook. Here we handle new telegram messages
    :return: (message, status_code)
    :rtype: tuple
    """
    if request.is_json:
        print(request.get_json(force=True))
        return current_app.telegram.handle_request(request.get_json(force=True)), 200
    else:
        return jsonify({
            'status': 'error',
            'message': 'Accept only json'
        }), 400
