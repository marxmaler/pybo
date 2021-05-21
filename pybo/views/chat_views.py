from flask import Blueprint, render_template
bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/bot')
def bot():
    return render_template('chat/chatbot.html')