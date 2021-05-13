from flask import Blueprint, render_template, url_for #url 관리 패키지
from pybo.models import Question, Answer, User
from datetime import datetime
from pybo import db #__init__에 선언한 db변수
import numpy
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/') #블루프린트 이름부터 설정
#여기 나오는 'main'은 임의의 값이지만, 보통은 관련성 있는 단어로 함.
#url_prefix는 특정 유형의 url들에 공통적으로 붙일 문자열

#블루프린트를 만들었으면 app.route()가 아니라 블루프린트변수명.route()
@bp.route('/test') #테스트 데이터 100개 생성
def test():
    for i in range(100):
        q = Question(subject='테스트 데이터 [%03d]'%i, content='내용무', create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/hello')
def hello_pybo():
    # q = Question.query.get(5)
    # a = Answer(question=q, content='답변 3번', create_date=datetime.now()) #question을 등록하면 자동으로 question_id가 들어감(question.id가 그리로 들어감)
    # db.session.add(a)
    # db.session.commit()
    #question_id가 2인 것만 조회하기
    # result = Answer.query.filter(Answer.question_id==2).all()
    # result = q.answer_set
    # print(result)

    # for i in range(1,6):
    #     a = Answer(question=q, content=f'답변 {i}번', create_date=datetime.now())
    #     db.session.add(a)
    #
    # db.session.commit()
    #
    # print(q.answer_set)
    # men = User.query.filter(User.sex==1, User.age>18).all()
    # women = User.query.filter(User.sex==2, User.age>18).all()
    # boys = User.query.filter(User.sex==1, User.age<=18).all()
    # girls = User.query.filter(User.sex==2, User.age<=18).all()
    # print(men)
    # print(women)
    # print(boys)
    # print(girls)
    # db.session.delete(q)
    # db.session.commit()
    return 'Hello, Pybo!'

@bp.route('/')
def index(): # 보통 주소 첫 화면을 index라고 함
    return redirect(url_for('question.call_question_list')) #여기서 question은 question_views에서 정의한 blueprint의 이름. call_question_list는 call_question_list()
