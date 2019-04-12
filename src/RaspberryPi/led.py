import sys, time
import RPi.GPIO as GPIO

redPin, greenPin, bluePin = 11, 13, 15

def blink(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	
def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def redOn():
	blink(redPin)

def greenOn():
	blink(greenPin)

def blueOn():
	blink(bluePin)

def yellowOn():
	blink(redPin)
	blink(greenPin)

def cyanOn():
	blink(greenPin)
	blink(bluePin)

def magentaOn():
	blink(redPin)
	blink(bluePin)

def whiteOn():
	blink(redPin)
	blink(greenPin)
	blink(bluePin)

def redOff():
	turnOff(redPin)

def greenOff():
	turnOff(greenPin)

def blueOff():
	turnOff(bluePin)

def yellowOff():
	turnOff(redPin)
	turnOff(greenPin)

def cyanOff():
	turnOff(greenPin)
	turnOff(bluePin)

def magentaOff():
	turnOff(redPin)
	turnOff(bluePin)

def whiteOff():
	turnOff(redPin)
	turnOff(greenPin)
	turnOff(bluePin)


def redBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(redPin)
		time.sleep(0.5)
		turnOff(redPin)
		time.sleep(0.5)	
	turnOff(redPin)

def greenBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(greenPin)
		time.sleep(0.5)
		turnOff(greenPin)
		time.sleep(0.5)	
	turnOff(greenPin)

def blueBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(bluePin)
		time.sleep(0.5)
		turnOff(bluePin)
		time.sleep(0.5)	
	turnOff(bluePin)

def yellowBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(redPin)
		blink(greenPin)
		time.sleep(0.5)
		turnOff(redPin)
		turnOff(greenPin)
		time.sleep(0.5)	
	turnOff(redPin)
	turnOff(greenPin)

def cyanBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(greenPin)
		blink(bluePin)
		time.sleep(0.5)
		turnOff(greenPin)
		turnOff(bluePin)
		time.sleep(0.5)	
	turnOff(greenPin)
	turnOff(bluePin)

def magentaBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(redPin)
		blink(bluePin)
		time.sleep(0.5)
		turnOff(redPin)
		turnOff(bluePin)
		time.sleep(0.5)	
	turnOff(redPin)
	turnOff(bluePin)
def whiteBlink(sec):
	startTime = time.time()
	while time.time() - startTime - sec < 0:
		blink(redPin)
		blink(greenPin)
		blink(bluePin)
		time.sleep(0.5)
		turnOff(redPin)
		turnOff(greenPin)
		turnOff(bluePin)
		time.sleep(0.5)	
	turnOff(redPin)
	turnOff(greenPin)
	turnOff(bluePin)
if __name__ == "__main__":
	while True:
		cmd = raw_input("Choose an option: ")

		if cmd == "red on":
			redOn()

		elif cmd == "red off":
			redOff()

		elif cmd == "green on":
			greenOn()

		elif cmd == "green off":
			greenOff()

		elif cmd == "blue on":
			blueOn()
		
		elif cmd == "blue off":
			blueOff()

		elif cmd == "yellow on":
			yellowOn()

		elif cmd == "yellow off":
			yellowOff()

		elif cmd == "cyan on":
			cyanOn()

		elif cmd == "cyan off":
			cyanOff()

		elif cmd == "magenta on":
			magentaOn()

		elif cmd == "magenta off":
			magentaOff()

		elif cmd == "white on":
			whiteOn()

		elif cmd == "white off":
			whiteOff()
		
		elif cmd == "red blink":
			redBlink(3.5)

		elif cmd == "green blink":
			greenBlink(3)

		elif cmd == "blue blink":
			blueBlink(3)

		elif cmd == "yellow blink":
			yellowBlink(3)

		elif cmd == "cyan blink":
			cyanBlink(3)

		elif cmd == "magenta blink":
			magentaBlink(3)

		elif cmd == "white blink":
			whiteBlink(3)

		elif cmd == 'quit':
			redOff()
			greenOff()
			blueOff()			
			break
		else:
			print("Not a valid command.")
	