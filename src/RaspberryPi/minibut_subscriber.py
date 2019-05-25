import paho.mqtt.client as mqtt
import LCD_driver
import led
import time

# Subscriber callback
def on_connect(client, userdata, flags, rc):
   print('Connected wiht broker server')
   client.subscribe('A-0001/server')
   print('Connected with result code' + str(rc))

def on_message(client, userdata, message):
    print("message recievied")
    decodedMessage = str(message.payload.decode('utf-8'))
    grade= decodedMessage.split(',')[0]
    window = decodedMessage.split(',')[1]
    machine = decodedMessage.split(',')[2]
    pm10 = decodedMessage.split(',')[3]
    pm25 = decodedMessage.split(',')[4]

    print(grade, window, machine, pm10, pm25)

    myLCD = LCD_driver.lcd()
    myLED = led.led()
    myLCD.lcd_display_device(int(machine), int(window))

    time.sleep(3)

    myLCD.lcd_clear()
    time.sleep(0.5)

    myLCD.lcd_display_dust(float(pm10), float(pm25))

    myLED.redOff()
    myLED.greenOff()
    myLED.yellowOff()
    myLED.blueOff()

    grade = int(grade)

    if grade == 1:
        myLED.blueOn()
    elif grade == 2:
        myLED.greenOn()
    elif grade == 3:
        myLED.yellowOn()
    else:
        myLED.redOn()

# Subscriber
broker_address="54.180.181.189"
client1 = mqtt.Client("ClientSubscriber")

client1.on_connect = on_connect
client1.on_message = on_message

client1.connect(broker_address)

client1.loop_forever()
