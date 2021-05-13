from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from pybo.models import Question
from .. import db
from ..forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list')
def call_question_list():
    page = request.args.get('page', type=int, default=1) #웹페이지에서 페이지 값을 받아오도록, 값이 주어지지 않으면 기본값 1로 설정.
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10) #per_page=10는 한 페이지 당 10개를 보여준다는 뜻
    return render_template('question/question_list.html', question_list=question_list)  # flask에서 import 해줘야 쓸 수 있음(templates 폴더 내의 해당 html page를 반환 - 즉, 이동시켜줌. 여기서는 question폴더 내의 question_list.html 파일)
    # question_list=question_list 부분은 해당 웹페이지에서 이 코드의 question_list 값을 동일하게 question_list라는 변수에 넣어쓰겠다는 뜻(변수는 여러 개 가능)

@bp.route('/detail/<int:question_id>') #detail 뒤에 int형 데이터가 입력되면 question_id라는 변수에 저장해라
def detail(question_id):
    # question = Question.query.get(question_id)
    form = AnswerForm()
    question = Question.query.get_or_404(question_id) #get 실패하면 404 오류 메시지를 띄우는 메서드
    return render_template('question/detail.html', question=question, form=form) #flask에서 import 해줘야 쓸 수 있음(templates 폴더 내의 해당 html page를 반환 - 즉, 이동시켜줌. 여기서는 question폴더 내의 question_list.html 파일)
    # question_list=question_list 부분은 해당 웹페이지에서 이 코드의 question_list 값을 동일하게 question_list라는 변수에 넣어쓰겠다는 뜻(변수는 여러 개 가능)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = QuestionForm()

    if request.method == "POST" and form.validate_on_submit():
        #request 방식이 post이고 전송된 form의 데이터가 적합할 때
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)