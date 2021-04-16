import requests
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime
import threading
import time

# db config
config = {
    "host": "wth-stk-svc.chik9zpsmeh8.us-east-1.rds.amazonaws.com",
    "port": 3306,
    "user": "admin",
    "password": "asdf555!",
    "database": "multicampus"
}


# db삽입
def weather_quary(temp, updated_time):
    con = pymysql.connect(**config)
    cur = con.cursor()
    print(temp,updated_time)

    cur.execute("SELECT updated_time FROM Weathers WHERE updated_time='{}'".format(updated_time))

    exists_data = cur.fetchall()
    if not exists_data:
        sql = "INSERT INTO Weathers(temp,updated_time) VALUES({},'{}')"

        sql = sql.format(temp, updated_time)

        cur.execute(sql)
        con.commit()
        print(updated_time + 'quary success')
    else:
        return 1

    return 0

def weather():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    # pprint(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')

    data1 = soup.find('div', {'class': 'weather_box'})

    find_address = "서울특별시"
    print('현재 위치: ' + find_address)

    find_currenttemp = data1.find('span', {'class': 'todaytemp'}).text
    print('현재 온도: ' + find_currenttemp + '℃')

    updated_time = "{:%Y-%m-%d-%H-%M}".format(datetime.now())

    weather_quary(find_currenttemp,updated_time)

weather()