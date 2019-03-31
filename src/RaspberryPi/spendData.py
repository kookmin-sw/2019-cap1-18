import datetime as dt
import paho.mqtt.client as mqtt
import time
import json


count = 0

#mqtt publisher
broker_address="192.168.34.80"
client2 = mqtt.Client("ClientPublisher")
client2.connect(broker_address)


while True:
	time.sleep(60)
	count += 1

	data = open('aqi.json', 'r').read()
	data = json.loads(data)

	data_size = len(data) -1

	pub_data="{0},{1}".format(count, data[data_size])

#mqtt publisher
	client2.publish("vds1/data",pub_data)

	print("Data Spend")
	print("[{0}] {1}".format(count, data[data_size]))
