import paho.mqtt.client as mqtt
import time
import json
import aqi
import LCD_driver

# Mqtt publisher
broker_address="54.180.181.189"
client2 = mqtt.Client("ClientPublisher")
client2.connect(broker_address)

# LCD object and variables
myLcd = LCD_driver.lcd()
pm10, pm25 = 0, 0
values = []

while True:
    # Air quality sensor On
    aqi.cmd_set_sleep(0)
    aqi.cmd_set_mode(1)

    for t in range(15):
        values = aqi.cmd_query_data()
        if values is not None:
            #print("PM2.5: ", values[0], ", PM10: ", values[1])
            time.sleep(2)

    pm25, pm10 = values[0], values[1]

    #Open stored data file
    with open('aqi.json') as json_data:
        data = json.load(json_data)

    # Check if length is more than 100 and delete first element
    if len(data) > 100:
        data.pop(0)

    # Append new values
    dataToSend = {'pm25': values[0], 'pm10': values[1], 'time': time.strftime("%d.%m.%Y %H:%M:%S")}
    data.append(dataToSend)

    # Save it
    with open('aqi.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

    data = open('aqi.json', 'r').read()
    data = json.loads(data)
    #data_size = len(data) -1

    #dict_data = data[data_size]
    dict_data = data[-1]
    pm10 = dict_data['pm10']
    pm25 = dict_data['pm25']

    print(pm10, pm25)

    #myLcd.lcd_display_dust(pm10, pm25)

    pub_data = dataToSend = 'pm25: ' + str(pm25) + ', ' + 'pm10: ' + str(pm10) + ', date: ' + time.strftime("%d.%m.%Y %H:%M:%S")
    #pub_data="{0},{1}".format(count, data[data_size])

    #mqtt publisher
    client2.publish("A-0001/rpi",pub_data)

    print("Data Send")

    time.sleep(30)
    #print("[{0}] {1}".format(count, data[data_size]))
