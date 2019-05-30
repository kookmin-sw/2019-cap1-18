import datetime as dt
import paho.mqtt.client as mqtt
import time
import json

# count = 0

#mqtt publisher
broker_address="192.168.0.3"
client2 = mqtt.Client("ClientPublisher")
client2.connect(broker_address)

while True:
    time.sleep(60)

    # count += 1

    data = open('aqi.json', 'r').read()
    data = json.loads(data)
    data_size = len(data) -1

    dict_data = data[data_size]
    pm10 = dict_data['pm10']
    pm25 = dict_data['pm25']

    pub_data = dataToSend = 'pm25: ' + str(pm25) + ', ' + 'pm10: ' + str(pm10) + ', date: ' + time.strftime("%d.%m.%Y %H:%M:%S")
    #pub_data="{0},{1}".format(count, data[data_size])

    #mqtt publisher
    client2.publish("userID/rpi",pub_data)

    print("Data Send")
    #print("[{0}] {1}".format(count, data[data_size]))

    #data.close()