# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json

def naverbook(bookname):

    client_id = "ThErcuAnOGY5AkYlwZ1i"
    client_secret = "JM0ANJuRDb"
    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        response_body = response_body.decode('utf-8')
        jsontemp = json.loads(response_body)  # 그냥 읽으려니까 안읽혀서 json 형식으로 바꿔줌
        # items = jsontemp['items']
        # for item in items:
        #     print(item['title'])


        # booklist = []
        # for temp in response_body['items']:
        #     # print(temp)
        #     title = temp['title'].replace('<b>','').replace('</b>','')
        #     author = temp['author']
        #     price = temp['price']
        #     publisher = temp['publisher']
        #     pubdate = temp['pubdate']
        #     booklist.append({'title': title,
        #                      'author': author,
        #                      'price': price,
        #                      'publisher': publisher,
        #                      'pubdate': pubdate})

    else:
        print("Error Code:" + rescode)
        # sys.exit(0)



    return jsontemp

# jsondata = '''{"title":"삼국지", "price":500}''' # 완벽한 json 데이터가 아니어서 {} 안에 쌍따옴표 안쓰면 디코드 에러남
#
# result = json.loads(jsondata) #json 형태로 된 데이터를 파싱할 수 있게 만들어줌
#
# title_data = result['title']
# print(title_data)

# jsonString = '''
# {"date":"2021-05-11" , "data":[{"price":300 , "total":20},{"price":100 , "total":120},{"price":1200 , "total":52}]}
# '''
#
# temp = json.loads(jsonString)
# datas = temp['data']
# print(datas)
# totalPrice = 0
# for data in datas:
#     totalPrice += data['price']*data['total']
#
# print(totalPrice)

def navermovie(moviename):

    client_id = "ThErcuAnOGY5AkYlwZ1i"
    client_secret = "JM0ANJuRDb"
    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        response_body = response_body.decode('utf-8')
        jsontemp = json.loads(response_body)  # 그냥 읽으려니까 안읽혀서 json 형식으로 바꿔줌

    else:
        print("Error Code:" + rescode)
        # sys.exit(0)



    return jsontemp

def navershop(productname):

    client_id = "ThErcuAnOGY5AkYlwZ1i"
    client_secret = "JM0ANJuRDb"
    encText = urllib.parse.quote(productname)
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        response_body = response_body.decode('utf-8')
        jsontemp = json.loads(response_body)  # 그냥 읽으려니까 안읽혀서 json 형식으로 바꿔줌

    else:
        print("Error Code:" + rescode)
        # sys.exit(0)


    print(jsontemp)
    return jsontemp
