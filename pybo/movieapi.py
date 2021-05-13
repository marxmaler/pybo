import requests
from bs4 import BeautifulSoup as bs
import sys
import re
import os

def collect_movie_data():
    url = 'https://movie.naver.com/movie/running/current.nhn'
    html = requests.get(url)

    if html.status_code != 200:
        sys.exit('데이터를 가져오지 못했습니다')
    soup = bs(html.text, features='html.parser')
    # 또는 soup = bs(html, 'lxml') - lxml 설치하고 써야함
    #
    #
    # 이미지
    thumbs = soup.findAll('div', 'thumb') #class_=는 생략 가능
    img_list = []
    for thumb in thumbs:
        img_list.append(thumb.find('img')['src'])

    title_list = []
    score_list = []
    genre_list = []

    dls = soup.findAll('dl', 'lst_dsc')
    for dl in dls:
        title_list.append(dl.find('dt', 'tit').find('a').text)
        score_list.append(dl.find('div', 'star_t1').find('span', 'num').text)
        temps = dl.find('span', 'link_txt').find_all('a')
        genre = ''
        for temp in temps:
            if len(genre) > 0:
                genre += '/'
            genre += temp.text
        genre_list.append(genre)

    movie_infoes = []
    # print(genre_list)
    for i in range(len(title_list)):
        movie_infoes.append({'img':img_list[i], 'title':title_list[i], 'score':score_list[i], 'genre':genre_list[i]})

    # print(movie_infoes)
    return movie_infoes
