import requests
import json
from bs4 import BeautifulSoup as bs
import datetime
import sys

def get_wdata(region):
    date = str(datetime.datetime.now().date()).replace('-','.')
    time = str(datetime.datetime.now().time().hour)
    url = 'https://www.weather.go.kr/weather/observation/currentweather.jsp?auto_man=m&stn=0&type=t99&reg=100&x=32&y=11' \
          '&tm=' + date+'.'+time

    html = requests.get(url)
    if html.status_code != 200:
        sys.exit('데이터를 가져오지 못했습니다')
    soup = bs(html.text, features='html.parser')

    trs = soup.findAll('tr')
    object_tr = ''
    cnt = 1
    for tr in trs:
        if cnt < 3:
            cnt += 1
            continue
        temp_region = tr.find('a').text
        if region == temp_region:
            object_tr = tr
            region = temp_region

    cnt = 1
    if object_tr == '':
        for tr in trs:
            if cnt < 3:
                cnt += 1
                continue
            temp_region = tr.find('a').text
            if region in temp_region:
                object_tr = tr
                region = temp_region

    if object_tr == '':
        return '지역명이 잘못 되었습니다.'

    tds = object_tr.findAll('td')
    currentWeather = tds[1].text
    currentTemp = tds[5].text
    currentPrecip = tds[8].text

    if len(currentPrecip) < 2:
        currentPrecip = '0.0'

    if len(currentWeather) < 2:
        if float(currentPrecip) > 0:
            currentWeather = '우천'
        else:
            currentWeather = '맑음'


    return region + '의 현재 날씨 정보입니다. ' + '현재 날씨는 ' + currentWeather + '이며, 기온은 ' + currentTemp + ', 강수량은 ' + currentPrecip + '입니다.'


# print(get_wdata('서울'))