from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# StringField는 글자수 제한 있어서 주로 제목 입력할 때 쓰고
# TextField는 내용 입력할 때 씀

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()]) #validators는 이 데이터가 필수 항목인지 체크하고, 검증하는 부분
    content = TextField('내용', validators=[DataRequired()])


class AnswerForm(FlaskForm):
    content = TextField('내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class NaverBookForm(FlaskForm):
    search = StringField('검색창', validators=[DataRequired()])

class NaverMovieForm(FlaskForm):
    search = StringField('검색창', validators=[DataRequired()])
    
class HelpForm(FlaskForm):
    search = StringField('검색', validators=[DataRequired()])