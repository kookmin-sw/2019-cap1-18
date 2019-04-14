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

 #60분 단위로 실행
 time.sleep(3600)

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

 #저장한 값 출력
 #print("data time : " + dataTime.text)
 #print("pm10 Value : " + pm10Value.text)
 #print("pm25 Value : " + pm25Value.text)
 #print("pm10 Grade : " + pm10Grade.text)
 #print("pm25 Grade : " + pm25Grade.text + "\n")

 #DB저장 코드
 # mongodb 와 python 연결
 conn = pymongo.MongoClient('127.0.0.1', 27017)
 db = conn.get_database('dust')
 collection = db.get_collection('api')

 #저장된 값 출력
 #results = collection.find()
 #print ("이전 db 값")
 #for result in results:
 # print (result)
 #print ("\n")

 #api 값 저장
 collection.insert({"date": dataTime.text, "pm10value" : pm10Value.text, "pm25value": pm25Value.text, "pm10grade": pm10Grade.text, "pm25grade": pm25Grade.text})

 #새로 저장된 값 출력
 #results = collection.find()
 #print("이후 db값")
 #for result in results:
 # print (result)

 #접속 해제
 conn.close()
