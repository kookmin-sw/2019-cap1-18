topic = "1,{'pm10': 11.7, 'time': '29.03.2019 07:51:59', 'pm25': 9.3}"

print(topic)

topic = topic.split(', ')
print(topic)

pm10 = "pm10"
pm25 = "pm25"
time = "time"

index = len(topic)

for i in [0,1,2]:
 if 'pm10' in topic[i]:
  pm10 = topic[i]
  pm10 = pm10[8:]
  print(pm10)

 if 'pm25' in topic[i]:
  pm25 = topic[i]
  pm25 = pm25[8:]
  print(pm25)

 if 'time' in topic[i]:
  time = topic[i]
  time = time[9:28]
  print(time)
