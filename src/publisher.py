import datetime as dt
import paho.mqtt.client as mqtt
import time
import json
from pymongo import MongoClient


count = 0

### mongoDB 연동 ###
client = MongoClient()
client = MongoClient('127.0.0.1', 27017)
db = client.get_database('dust')
controlCol = db.get_collection('control')
recentCol = db.get_collection('recent')
recentUserDatas = recentCol.find()

#mqtt publisher
broker_address="192.168.34.80"
client2 = mqtt.Client("ClientPublisher")
client2.connect(broker_address)


while True:
	for userData in recentUserDatas:
		userid = userData["idnum"]
		grade10 = userData["ipm10grade"]
		grade25 = userData["ipm25grade"]
		grade = max([grade10, grade25])
		ipm10 = userData["ipm10value"]
		ipm25 = userData["ipm25value"]

		userCtlData = controlCol.find_one({"idnum":userid})

		window = userCtlData["window"]
		machine = userCtlData["machine"]


		pub_data = "{0}, {1}, {2}, {3}, {4}".format(grade, window, machine, ipm10, ipm25)

		#mqtt publisher
		client2.publish("{0}/server".format(userid), pub_data)

		print("Data Send: {0}".format(userid))
		print("{1}".format(pub_data))
	time.sleep(60)
