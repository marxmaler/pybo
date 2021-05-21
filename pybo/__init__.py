from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

#sqlalchemy db 설정(이 3줄이 한 묶음)
app.config.from_object(config) # 플라스크 환경 설정
db.init_app(app)
migrate.init_app(app, db)

from . import models #.은 같은 폴더 내에서 찾으라는 뜻
#db 생성하는 코드가 위 3줄이어서

#여기에 내가 만든 블루프린트를 사용할 거라고 등록을 시켜줘야 쓸 수 있음
from .views import main_views, naver_views, question_views, answer_views, auth_views, movie_views, chat_views
app.register_blueprint(main_views.bp)
app.register_blueprint(naver_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(chat_views.bp)
from .filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime


# 보안상 취약하지만 이렇게 하는 것도 가능
# app = Flask(__name__)
#
# app.config.from_object(config)  # 플라스크 환경 설정
# db.init_app(app)
# migrate.init_app(app, db)
#
# from . import models  # .은 같은 폴더 내에서 찾으라는 뜻
#
# # 여기에 내가 만든 블루프린트를 사용할 거라고 등록을 시켜줘야 쓸 수 있음
# from .views import main_views, naver_views
#
# app.register_blueprint(main_views.bp)
# app.register_blueprint(naver_views.bp)

