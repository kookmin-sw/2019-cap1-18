import paho.mqtt.client as mqtt
import pymongo
import time
import string

#전역변수
data = ""
pm10 = ""
pm25 = ""
date = ""
pm10grade = ""
pm25grade = ""


def storeData():
 global data
 global pm10
 global pm25
 global date
 global pm10grade
 global pm25grade

 if(len(data) > 1):
  pm10 = float(pm10[0:])
  pm25 = float(pm25[0:])
  date = str(date[0:])


  if(pm10 <= float(30.0)):
   pm10grade = int(1)
  elif(pm10 <= float(80.0)):
   pm10grade = int(2)
  elif(pm10 <= float(150.0)):
   pm10grade = int(3)
  else:
   pm10grade = int(4)

  if(pm25 <= float(15.0)):
   pm25grade = int(1)
  elif(pm25 <= float(35.0)):
   pm25grade = int(2)
  elif(pm25 <= float(75.0)):
   pm25grade = int(3)
  else:
   pm25grade = int(4)


  conn = pymongo.MongoClient('127.0.0.1', 27017)
  db = conn.get_database('dust')

  collection = db.get_collection('internaldust')
  collection.insert({"idnum": "A-0001", "ilat": 37.607694, "ilng": 127.000080, "ipm10value": pm10, "ipm10grade": pm10grade, "ipm25value": pm25, "ipm25grade": pm25grade, "idate": date[0:]})

  collection = db.get_collection('recent')

  #idate update 시 capped 확인
  collection.update({"idnum": "A-0001"}, {"$set": {"ilat": 37.607964, "ilng": 127.000080, "ipm10value": pm10, "ipm10grade": pm10grade, "ipm25value": pm25, "ipm25grade": pm25grade, "idate": date}})

  conn.close()

 data = None

#subscriber callback
def on_message(client, userdata, message):
# print("message recived ",str(message.payload.decode("utf-8")))
# print("message topic=",message.topic)
# print("message qos=",message.qos)
# print("message retain flag=", message.retain)

 #data split
 global data
 global pm10
 global pm25
 global date
 data = str(message.payload.decode("utf-8"))
 data = data.split(', ')

 # pm25, pm10, time

 pm25 = data[0]
 pm25 = pm25[6:]
 #print(pm25)

 pm10 = data[1]
 pm10 = pm10[6:]
 #print(pm10)

 date = data[2]
 date = date[6:]
 #print(date)

 storeData()
 #print("finish")

# subscriber
broker_address="54.180.181.189"

client1 = mqtt.Client("ServerSubsriber")
client1.connect(broker_address)

client1.subscribe("A-0001/rpi")
client1.on_message = on_message


client1.loop_forever()

#while True:
# client1.subscribe("A-0001/rpi")
# client1.on_message = on_message
# client1.loop()
# storeData()
