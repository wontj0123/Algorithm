import json
from datetime import datetime
import requests
import xmltodict

apikey = "1IW4Ombd5ZAaLvd43nz9F%2F3ZoQxQ1C7nRtGh%2FOCAIvyZzDdNxHi9hN4w0%2BHcl22kZ5%2BZttUiSASiXM9TRaDBog%3D%3D"
currentDate="{:%Y%m%d}".format(datetime.now())
currentTime="{:%H%M}".format(datetime.now())


url ="http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey={}&numOfRows=10&pageNo=1&base_date={}&base_time=0200&nx=60&ny=127".format(apikey,currentDate)

content = requests.get(url).content
dict = xmltodict.parse(content)
print(dict['response']['body'])
jsonString = json.dumps(dict['response']['body'])
jsonObj = json.loads(jsonString)

category = ""
for item in jsonObj['items']['item']:
    category = item['category']
    if category == "T3H":
        print(item['fcstValue'])
print(currentTime)
