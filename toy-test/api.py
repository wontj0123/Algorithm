import requests, json, xmltodict
from datetime import datetime
#import BeautifulSoup
#import threading
#import time



apikey = "1IW4Ombd5ZAaLvd43nz9F%2F3ZoQxQ1C7nRtGh%2FOCAIvyZzDdNxHi9hN4w0%2BHcl22kZ5%2BZttUiSASiXM9TRaDBog%3D%3D"
currentDate="{:%Y%m%d}".format(datetime.now())
currentTime="{:%H%M}".format(datetime.now())

url ="http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey={}&numOfRows=10&pageNo=1&base_date={}&base_time=0200&nx=60&ny=127".format(apikey,currentDate)
#read = requests.get(url=)
content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['response']['body'])
jsonObj = json.loads(jsonString)

for item in jsonObj['items']['item']:
    print(item)

print(currentTime)
print(currentDate)
print(jsonObj)

#json_structured_data = json.loads(read.text)

#http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=1IW4Ombd5ZAaLvd43nz9F%2F3ZoQxQ1C7nRtGh%2FOCAIvyZzDdNxHi9hN4w0%2BHcl22kZ5%2BZttUiSASiXM9TRaDBog%3D%3D&numOfRows=10&pageNo=1&base_date=20210416&base_time=0230&nx=60&ny=127
