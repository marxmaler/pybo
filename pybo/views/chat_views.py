from flask import Blueprint, render_template, request, redirect, url_for
from ..forms import HelpForm
from pybo.dialogflowapi import chat

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/bot')
def bot():
    return render_template('chat/chatbot.html')

@bp.route('/help', methods=('GET','POST'))
def help():
    form = HelpForm()
    if request.method == "POST" and form.validate_on_submit():
        result = chat(form.search.data, '1234')
        if result == '영화 순위 메뉴':
            return redirect(url_for('movie.movie_rank'))
        elif result == '구글':
            return redirect('http://www.google.co.kr')

    return render_template('chat/help.html', form=form)