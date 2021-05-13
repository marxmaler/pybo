from pybo import db

class Question(db.Model): #SQLAlchemy의 Model을 인자로 받음. DB에서 Question이라는 테이블을 생성하는 것과 동일
    id = db.Column(db.Integer, primary_key=True) #이 변수들을 각각 Question 테이블의 컬럼이 됨
    subject = db.Column(db.String(200), nullable=False) #여기서 200은 사이즈 제한
    content = db.Column(db.Text(), nullable=False) # String과 달리 Text는 글자 수 제한이 없음
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) #외래키, Question의 PK값(id)을 사용, 질문 삭제되면 같이 삭제되도록 설정
    question = db.relationship('Question', backref=db.backref('answer_set')) #컬럼이 아니고 관계(역참조 - question_id가 똑같은 답변들은 해당 id의 질문을 참조하여 하나로 묶어줌)
    #즉, 어떤 질문에 대한 답변인지 나타내기 위한 것
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False) #unique=True는 중복값 쓸 수 없게 하는 조항
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)