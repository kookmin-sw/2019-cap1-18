import requests
import json
import datetime
import time
import pymongo


while True:
 headers = {'x-api-key': 'qIowMCREj07g4hEvqDAX65Qn2HZtdI201DW6UE5N', 'accept': 'application/json'}
 url = 'https://fqzj7zros6.execute-api.ap-northeast-2.amazonaws.com/Beta/device?ne=37.607964%2C%20127.000080&count=5'
 response = requests.get(url=url, headers=headers)

 if response.status_code != 200 :
  print("error {0}", response.status_code)
  time.sleep(360)
  continue

 data = response.text
 device = []
 lat = []
 lng = []

 dict = json.loads(response.text)


 #print(dict['results'][1]['device'])

 for i in range(5) :
  device.append(dict['results'][i]['device'])
  lat.append(dict['results'][i]['lat'])
  lng.append(dict['results'][i]['long'])
  #print("{0} {1} {2}".format(device[i], lat[i], lng[i]))


 for i in [2,3,4]:
  url = 'https://fqzj7zros6.execute-api.ap-northeast-2.amazonaws.com/Beta/air?device=' + device[i] + '&count=5'
  response = requests.get(url=url, headers=headers)

  if response.status_code != 200 :
   print("error {0}", response.status_code)
   time.sleep(360)
   continue

  dict = json.loads(response.text)

  pm25 = dict['results'][0]['pm25']
  pm10 = dict['results'][0]['pm10']
  date = dict['results'][0]['timestamp']
  date = datetime.datetime.fromtimestamp(date/1000)
  date = date.strftime('%Y-%m-%d %H:%M:%S')


  if pm10 <= float(30.0) :
   pm10grade = 1
  elif pm10 <= float(80.0) :
   pm10grade = 2
  elif pm10 <= float(150.0) :
   pm10grade = 3
  else :
   pm10grade = 4

  if pm25 <= float(15.0) :
   pm25grade = 1
  elif pm25 <= float(35.0) :
   pm25grade = 2
  elif pm25 <= float(75.0) :
   pm25grade = 3
  else :
   pm25grade = 4


  conn = pymongo.MongoClient('127.0.0.1', 27017)
  db = conn.get_database('dust')
  collection = db.get_collection('kookmindust')

  collection.insert({"device":device[i], "elat":float(lat[i]), "elng":float(lng[i]), "epm10value": pm10, "epm10grade": pm10grade, "epm25value": pm25, "epm25grade": pm25grade, "edate": date})

  conn.close()
  #for문 종료

 print("ok")
 time.sleep(360)

