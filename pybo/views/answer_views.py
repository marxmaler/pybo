from flask import Blueprint, request, url_for, render_template
from pybo import db
from pybo.forms import AnswerForm
from pybo.models import Question, Answer
from datetime import datetime
from werkzeug.utils import redirect
bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit(): #form에 오류가 없으면

        content = request.form['content']

        answer = Answer(content=content, create_date=datetime.now())
        question.answer_set.append(answer) #db.session.add(answer)까지 포함된 방법
        db.session.commit()

        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/detail.html', question=question, form=form)