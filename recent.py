import pymongo
import json
import datetime
from pytz import timezone
from math import radians, cos, sin, asin, sqrt
import time

def calcdistance(lat1, long1, lat2, long2):
 long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])
 dlong = long2 - long1
 dlat = lat2 - lat1
 a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
 c = 2 * asin(sqrt(a))
 km = 6367 * c
 return km

while True:

 conn = pymongo.MongoClient('127.0.0.1', 27017)
 db = conn.get_database('dust')

 collection = db.get_collection('externaldust')
 eDatas = collection.find({"location": "정릉로"}).sort("_id", pymongo.DESCENDING).limit(1)
 # print(eDatas[0])

 collection = db.get_collection('kookmindust')
 kDatas = collection.find({"device": "AirSensor20133219"}).sort("_id", pymongo.DESCENDING).limit(1)
 # print(kDatas[0])

 collection = db.get_collection('recent')
 uDatas = collection.find({"idnum": "A-0001"}).limit(1)
 # print(uDatas[0])

 # print(eDatas[0]['elat'],eDatas[0]['elng'],kDatas[0]['elat'],kDatas[0]['elng'],uDatas[0]['ilat'],uDatas[0]['ilng'])
 eLocation = calcdistance(uDatas[0]['ilat'], uDatas[0]['ilng'], eDatas[0]['elat'], eDatas[0]['elng'])
 kLocation = calcdistance(uDatas[0]['ilat'], uDatas[0]['ilng'], kDatas[0]['elat'], kDatas[0]['elng'])

 # print(eLocation, kLocation)

 if (kLocation <= eLocation):
  # first
  kDate_str = kDatas[0]['edate']
  kDate_obj = datetime.datetime.strptime(kDate_str, '%Y-%m-%d %H:%M:%S')
  kDate_obj = timezone('Asia/Seoul').localize(kDate_obj)
  nowDate = datetime.datetime.now(timezone('Asia/Seoul'))
  time_diff = (nowDate - kDate_obj).seconds

  if time_diff < 5400:  # 5400 = 1hour 30minutes
   # collection = dust.recent
   collection.update({"idnum": "A-0001"}, {
    "$set": {"elat": kDatas[0]['elat'], "elng": kDatas[0]['elng'], "epm10value": kDatas[0]['epm10value'],
             "epm10grade": kDatas[0]['epm10grade'], "epm25value": kDatas[0]['epm25value'],
             "epm25grade": kDatas[0]['epm25grade'], "edate": kDatas[0]['edate']}})

  else:
   # second
   eDate = eDatas[0]['edate']
   eDate_str = eDatas[0]['edate']
   eDate_obj = datetime.datetime.strptime(eDate_str, '%Y-%m-%d %H:%M')
   eDate_obj = timezone('Asia/Seoul').localize(eDate_obj)
   nowDate = datetime.datetime.now(timezone('Asia/Seoul'))
   time_diff = (nowDate - eDate_obj).seconds

   if time_diff < 5400:
    collection.update({"idnum": "A-0001"}, {
     "$set": {"elat": eDatas[0]['elat'], "elng": eDatas[0]['elng'], "epm10value": eDatas[0]['epm10value'],
              "epm10grade": eDatas[0]['epm10grade'], "epm25value": eDatas[0]['epm25value'],
              "epm25grade": eDatas[0]['epm25grade'], "edate": eDatas[0]['edate']}})

   else:
   # 3th
    collection.update({"idnum": "A-0001"}, {
     "$set": {"elat": kDatas[0]['elat'], "elng": kDatas[0]['elng'], "epm10value": kDatas[0]['epm10value'],
              "epm10grade": kDatas[0]['epm10grade'], "epm25value": kDatas[0]['epm25value'],
              "epm25grade": kDatas[0]['epm25grade'], "edate": kDatas[0]['edate']}})

 conn.close()

 time.sleep(300)
