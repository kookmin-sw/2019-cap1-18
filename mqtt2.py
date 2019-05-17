import paho.mqtt.client as mqtt
import pymongo
import time

#전역변수
data = ""
pm10 = ""
pm25 = ""
date = ""

def storeData():
 global data
 global pm10
 global pm25
 global date

 if(len(data) > 1):
  pm10 = float(pm10[0:])
  pm25 = float(pm25[0:])
  date = (date[0:])

  print("store start " + date)
  conn = pymongo.MongoClient('127.0.0.1', 27017)
  db = conn.get_database('dust')

  collection = db.get_collection('internaldust')
  collection.insert({"idnum": "A-0001", "ilat": 37.603807, "ilng": 127.025997, "ipm10value": pm10, "ipm10grade": 0, "ipm25value": pm25, "ipm25grade": 0, "idate": date[0:]})

  collection = db.get_collection('recent')

  #idate update 시 자료형이 맞지 않아 오류
  collection.update({"idnum": "A-0001"}, {"$set": {"ilat": 37.603807, "ilng": 127.025997, "ipm10value": pm10, "ipm25value": pm25, "idate": date[0:]})

  conn.close()

 data = ""

"""
def splitData():
 global data
 global pm10
 global pm25
 global date

 print("split 출력")
 for i in [0,1,2,3,4,5]:
  if 'pm10' in data[i]:
   pm10 = data[i]
   pm10 = pm10[6:]
   #print(pm10)

  if 'pm25' in data[i]:
   pm25 = data[i]
   pm25 = pm25[6:]
   #print(pm25)

  if 'date' in data[i]:
   date = data[i]
   date = date[6:]
   print(date)
 print("here")
"""

#subscriber callback
def on_message(client, userdata, message):
 print("message recived ",str(message.payload.decode("utf-8")))
 print("message topic=",message.topic)
 print("message qos=",message.qos)
 print("message retain flag=", message.retain)

 #data split
 global data
 global pm10
 global pm25
 global date
 data = str(message.payload.decode("utf-8"))
 data = data.split(', ')

 for i in [0,1,2,3,4,5]:
  if 'pm10' in data[i]:
   pm10 = data[i]
   pm10 = pm10[6:]
   print(pm10)

  if 'pm25' in data[i]:
   pm25 = data[i]
   pm25 = pm25[6:]
   print(pm25)

  if 'date' in data[i]:
   date = data[i]
   date = date[6:]
   print(date)


# subscriber
broker_address="192.168.35.36"

client1 = mqtt.Client("ClientSubsriber")
client1.connect(broker_address)


while True:
 client1.subscribe("A-0001/rpi")
 client1.on_message = on_message
 client1.loop()

 storeData()
