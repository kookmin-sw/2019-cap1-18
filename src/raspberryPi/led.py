import sys, time
import RPi.GPIO as GPIO

redPin, greenPin, bluePin = 11, 13, 15

class led:
    def blink(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def turnOff(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def redOn(self):
        self.blink(redPin)

    def greenOn(self):
        self.blink(greenPin)

    def blueOn(self):
        self.blink(bluePin)

    def yellowOn(self):
        self.blink(redPin)
        self.blink(greenPin)

    def cyanOn(self):
        self.blink(greenPin)
        self.blink(bluePin)

    def magentaOn(self):
        self.blink(redPin)
        self.blink(bluePin)

    def whiteOn(self):
        self.blink(redPin)
        self.blink(greenPin)
        self.blink(bluePin)

    def redOff(self):
        self.turnOff(redPin)

    def greenOff(self):
        self.turnOff(greenPin)

    def blueOff(self):
        self.turnOff(bluePin)

    def yellowOff(self):
        self.turnOff(redPin)
        self.turnOff(greenPin)

    def cyanOff(self):
        self.turnOff(greenPin)
        self.turnOff(bluePin)

    def magentaOff(self):
        self.turnOff(redPin)
        self.turnOff(bluePin)

    def whiteOff(self):
        self.turnOff(redPin)
        self.turnOff(greenPin)
        self.turnOff(bluePin)

    def redBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(redPin)
            time.sleep(0.5)
            self.turnOff(redPin)
            time.sleep(0.5)
        self.turnOff(redPin)

    def greenBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(greenPin)
            time.sleep(0.5)
            self.turnOff(greenPin)
            time.sleep(0.5)
        self.turnOff(greenPin)

    def blueBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(bluePin)
            time.sleep(0.5)
            self.turnOff(bluePin)
            time.sleep(0.5)
        self.turnOff(bluePin)

    def yellowBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(redPin)
            self.blink(greenPin)
            time.sleep(0.5)
            self.turnOff(redPin)
            self.turnOff(greenPin)
            time.sleep(0.5)
        self.turnOff(redPin)
        self.turnOff(greenPin)

    def cyanBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(greenPin)
            self.blink(bluePin)
            time.sleep(0.5)
            self.turnOff(greenPin)
            self.turnOff(bluePin)
            time.sleep(0.5)
        self.turnOff(greenPin)
        self.turnOff(bluePin)

    def magentaBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(redPin)
            self.blink(bluePin)
            time.sleep(0.5)
            self.turnOff(redPin)
            self.turnOff(bluePin)
            time.sleep(0.5)
        self.turnOff(redPin)
        self.turnOff(bluePin)


    def whiteBlink(self, sec):
        startTime = time.time()
        while time.time() - startTime - sec < 0:
            self.blink(redPin)
            self.blink(greenPin)
            self.blink(bluePin)
            time.sleep(0.5)
            self.turnOff(redPin)
            self.turnOff(greenPin)
            self.turnOff(bluePin)
            time.sleep(0.5)
        self.turnOff(redPin)
        self.turnOff(greenPin)
        self.turnOff(bluePin)

'''
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
'''
