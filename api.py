import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymongo
import time

#값 저장 변수
dataTime = []
pm10Value = []
pm25Value = []
pm10Grade = []
pm25Grade = []

while True :

 #url을 통하여 크롤링
 url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=COgilT1y8qpGehRcfWiLgFfBJ9k%2B45OY%2BwCcRTLldJx%2BLNt9UJc1E0INNKTk7kYFwIzbQ9oXj%2B2ddoizfMH1Zw%3D%3D&numOfRows=1&pageNo=1&stationName=정릉로&dataTerm=DAILY&ver=1.3'
 req = requests.get(url)
 html = req.text
 soup = BeautifulSoup(html, 'html.parser')

 #원하는 태그의 값만 저장
 dataTime = soup.find('datatime')
 pm10Value = soup.find('pm10value')
 pm25Value = soup.find('pm25value')
 pm10Grade = soup.find('pm10grade')
 pm25Grade = soup.find('pm25grade')

#저장할 값 출력
#print("data time : " + dataTime.text)
#print("pm10 Value : " + pm10Value.text)
#print("pm25 Value : " + pm25Value.text)
#print("pm10 Grade : " + pm10Grade.text)
#print("pm25 Grade : " + pm25Grade.text + "\n")

 #DB저장 코드
 # mongodb 와 python 연결
 conn = pymongo.MongoClient('127.0.0.1', 27017)
 db = conn.get_database('dust')
 collection = db.get_collection('externaldust')

 try:
  pm10Value = float(pm10Value.text)
  pm10Grade = float(pm10Grade.text)
  pm25Value = float(pm25Value.text)
  pm25Grade = float(pm25Grade.text)
 except ValueError:
  print("except call")
  pm10Value = float(-1)
  pm10Grade = float(-1)
  pm25Value = float(-1)
  pm25Grade = float(-1)
 #api 값 저장
 collection.insert({"location": "정릉로", "elat": 37.603807, "elng": 127.025997, "epm10value" : pm10Value, "epm10grade": pm10Grade, "epm25value": pm25Value, "epm25grade": pm25Grade, "edate": dataTime.text})

#저장된 값 출력
#results = collection.find()
#print("이후 db값")
#for result in results:
# print (result)
 #close db connection
 conn.close()

 #60분 단위로 실행
 time.sleep(3600)

