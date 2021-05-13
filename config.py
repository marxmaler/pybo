import os

BASE_DIR = os.path.dirname(__file__) # 이 프로젝트의 경로 가져오기(내 컴퓨터일 때는 상관없지만 아마존 인스턴스 등에서 돌릴 때는 확인하기 어려우므로)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db')) # {} 부분에 format() 안에 들어있는 문자열 집어넣기
#os.path.join은 경로 합치기. 이 코드는 BASE_DIR에 pybo.db라는 파일이 있으면 그걸 쓰겠다는 얘기
#내 SQLite db에 접속하기 위한 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLALCHEMY의 이벤트 설정을 사용할 지 말지에 관한 것

SECRET_KEY = 'dev'

