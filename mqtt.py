import paho.mqtt.client as mqtt

#전역변수
data = ""
pm10 = ""
pm25 = ""
time = ""


#subscriber callback & data store
def on_message(client, userdata, message):
 print("message recived ",str(message.payload.decode("utf-8")))
 print("message topic=",message.topic)
 print("message qos=",message.qos)
 print("message retain flag=", message.retain)

 #data store
 global data
 data = str(message.payload.decode("utf-8"))
 data = data.split('{')
 data = data.split('}')
 data = data.split(', ')

 if(len(data)<3):
  print("error")
 else:
  for i in [0,1,2,3,4,5,6]:
   if 'pm10' in data[i]:
    global pm10
    pm10 = data[i]
    print(pm10)
    pm10 = pm10[8:]
    print(pm10)

   if 'pm25' in data[i]:
    global pm25
    pm25 = data[i]
    print(pm25)
    pm25 = pm25[8:]
    print(pm25)

   if 'time' in data[i]:
    global time
    time = data[i]
    print(time)
    time = time[9:25]
    print(time)

# subscriber
broker_address="192.168.34.80"

client1 = mqtt.Client("ClientSubsriber")
client1.connect(broker_address)
client1.subscribe("vds1/data")
client1.on_message = on_message
client1.loop_forever()

# rpi에서 받아온 값 잘라 각 변수에 넣기
#data = data.split(', ')

#print(data)

#if(len(data)<2):
# print("error")
#else:
# for i in [0,1,2]:
#  if 'pm10' in data[i]:
#   pm10 = data[i]
#   pm10 = pm10[8:]
#   print(pm10)

#  if 'pm25' in data[i]:
#   pm25 = data[i]
#   pm25 = pm25[9:28]
#   print(pm25)

#  if 'time' in data[i]:
#   time = data[i]
#   time = time[9:28]
#   print(time)
