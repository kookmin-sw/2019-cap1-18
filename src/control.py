from pymongo import MongoClient
import time

while True:

    ### mongoDB 연동 ###
    client = MongoClient()
    client = MongoClient('127.0.0.1', 27017)
    db = client.get_database('dust')
    settingCol = db.get_collection('setting')
    controlCol = db.get_collection('control')
    recentCol = db.get_collection('recent')
    recentUserDatas = recentCol.find()

    for userData in recentUserDatas:

        userid = userData["idnum"]
        ipm10 = userData["ipm10value"]
        ipm25 = userData["ipm25value"]
        ipm = max([ipm10, ipm25])
        epm10 = userData["epm10value"]
        epm25 = userData["epm25value"]
        epm = max([epm10, epm25])

        userSetData = settingCol.find_one({"idnum":userid})
        if userSetData == None:
            print("%s doesn't have Setting data".fomat(userid))
            continue

        userCtlData = controlCol.find_one({"idnum":userid})
        if userCtlData == None :
            print("%s doesn't have Control data".fomat(userid))
            continue

        cnt = userCtlData["cnt"]

        userValue = userSetData["userValue"]
        fixWin = userSetData["fixWin"]
        setWin = userSetData["setWin"]
        fixMach = userSetData["fixMatch"]
        setMach = userSetData["setMatch"]
        optSet = userSetData["optSet"]

        #실내 미세먼지, 실외 미세먼지 데이터 변수에 저장

        window  = 0
        machine = 0

        if fixWin : window = setWin
        if fixMach : machine = setMach
        if fixWin and fixMach :
            controlCol.replace_one({"idnum":userid}, {"idnum":userid, "window":window, "machine":machine}, upsert=True)
            cnt = 0
            continue         #창문, 공기청정기의 값이 모두 고정이 되어있다면 코드를 끝낸다.


        #추가기능 실행
        if optSet and ipm > 150 :
            if fixwin :
                if not window : machine = 1

            elif fixmach :
                if not machine : window = 1
                #counter가 있으면, 여기서 창문을 일정 시간 열고 닫는 형식우로 구현하기

            else :
                window = 1

            cnt = 0


        #기본
        elif cnt != 0 :
            cnt-=1
        elif ipm > int(userValue) :
            if ipm > epm :
                if fixWin :
                    if not window : machine = 1

                elif fixmach :
                    if not machine : window = 1

                else : window = 1

            else :
                if not window :
                    if not fixMach : machine = 1
            cnt = 3


        controlCol.replace_one({"idnum":userid}, {"idnum":userid, "window":window, "machine":machine, "cnt":cnt}, upsert=True)

    time.sleep(60)
