from pymongo import MongoClient
import time

client = MongoClient()

client = MongoClient('127.0.0.1', 27017)

db = client.get_database('dust')
collection = db.get_collection('recent')


recentUserDatas = collection.find()

for userData in recentUserDatas:
        print(userData["userid"])

        currIn = userData["internalData"]
        currExt = userData["externalData"]

        if currIn["pm10"] < currIn["pm25"]:
            inValue = currIn["pm25"]
        else:
            inValue = currIn["pm10"]

        if currExt["pm10"] < currExt["pm25"]:
            extValue = currExt["pm25"]
        else:
            extValue = currExt["pm10"]


        userValue = 10.0
        #userValue = userData["userValue"]

        control = {0, 0}        #window / machine 순서

        if inValue <= userValue:
            control = {0, 0}
            print("window is 0 and Machine is 0")
        elif inValue >= extValue:
            control = {0, 1}
            print("window is 0 and Machine is 1")
        else:
            control = {1, 0}
            print("window is 1 and Machine is 0")