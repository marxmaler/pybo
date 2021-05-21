from flask import Blueprint, render_template, url_for, request, jsonify  # url 관리 패키지
from pybo.models import Question, Answer, User
from datetime import datetime
from pybo import db #__init__에 선언한 db변수
import numpy
from werkzeug.utils import redirect
from pybo.movieapi import collect_movie_data
from pybo.naverapi import navermovie, navershop
from pybo.weatherapi import get_wdata

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

@bp.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json()
    # print(req)
    if req['queryResult']['intent']['displayName'] == 'movie ranking': #intent가 movie ranking이라면
        rankdata = collect_movie_data()
        result = ''
        count = 1
        for temp in rankdata:
            result = result + str(count) + '위: ' + temp['title'] + ' '
            if count == 3:
                break
            count += 1
        return {'fulfillmentText': result}

    if req['queryResult']['intent']['displayName'] == 'movie info - input_movie':
        movie_info = navermovie(req['queryResult']['queryText'])
        # movie_info = movie_info['items']
        movie_info = movie_info['items'][0]
        print(movie_info)

        # infos = []
        # for i in movie_info:
        #     movie_title = i['title'].replace('<b>','').replace('</b>','')
        #     subtitle = i['subtitle']
        #     pubDate = i['pubDate']
        #     director = i['director']
        #     actor = i['actor']
        #     userRating = i['userRating']
        #     info = '제목: ' + movie_title + '\n' + '부제: ' + subtitle + '\n' + '개봉: ' + pubDate + '\n' + '감독: ' + director + '\n' + \
        #            '출연: ' + actor + '\n' + '평점: ' + userRating + '\n'
        #     infos.append(info)
        #
        #     print_info = ''
        #     for info in infos:
        #         if infos[-1] != info:
        #             print_info += info + '=================================================================\n'
        #         else:
        #             print_info += info
        # return {'fulfillmentText': print_info}
        return movie_info_with_links(movie_info['image'], movie_info['title'].replace('<b>','').replace('</b>',''), movie_info['link'], '감독: ' + movie_info['director'] + ', 출연: ' + movie_info['actor'])

    if req['queryResult']['intent']['displayName'] == 'Weather - region':
        result = get_wdata(req['queryResult']['queryText'])
        return {'fulfillmentText': result}

    if req['queryResult']['intent']['displayName'] == 'Shop - search':
        result = navershop(req['queryResult']['queryText'])
        items = result['items']
        item_list = []
        for item in items:
            title = item['title']
            link = item['link']
            image = item['image']
            lprice = item['lprice']
            hprice = item['hprice']
            if hprice == '':
                hprice = lprice
            item_dic = {'title':title, 'link':link, 'image':image, 'lprice':lprice, 'hprice':hprice}
            item_list.append(item_dic)
        return shop_info_with_links(item_list)

    return {'fulfillmentText': '무슨 말인지 모르겠어요.'}

def movie_info_with_links(imgurl, title, link, subtitle):
    response_json = jsonify(
        fulfillment_text='영화정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [[
                        { # 이 부분 지우면 그림이 안나옴
                            "type": "image",
                            "rawUrl": imgurl
                        },
                        { # 이 부분 지우면 정보가 안나옴
                            "type": "info",
                            "title": title,
                            "actionLink": link,
                            "subtitle": subtitle
                        }
                    ]]
                }
            }
        ]
    )
    return response_json

# def movie_info_with_links(wdata):
#     response_json = jsonify(
#         fulfillment_text='영화정보'
#     )
#     return response_json
#참고로 이미지 같은 거 필요없으면 이렇게 텍스트만 처리해서 return해줄 수 있음.

def shop_info_with_links(item_list):
    richContents = []
    for item in item_list:
        richContent = [
            { # 이 부분 지우면 그림이 안나옴
                "type": "image",
                "rawUrl": item['image']
            },
            { # 이 부분 지우면 정보가 안나옴
                "type": "info",
                "title": item['title'].replace('<b>','').replace('</b>',''),
                "actionLink": item['link'],
                "subtitle": '최저가:' + item['lprice'] + ' 최고가:' + item['hprice']
            }
        ]
        richContents.append(richContent)

    response_json = jsonify(
        fulfillment_text='네이버 쇼핑 상품 정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": richContents
                }
            }
        ]
    )
    return response_json