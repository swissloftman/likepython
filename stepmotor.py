import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 4 # blau
coil_A_2_pin = 17 # pink
coil_B_1_pin = 23 # gelb
coil_B_2_pin = 24 # orange
#enable_pin   = 7 # Nur bei bestimmten Motoren benoetigt (+Zeile 24 und 30)

# anpassen, falls andere Sequenz
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,0,0,1]
Seq[1] = [0,0,1,1]
Seq[2] = [0,0,1,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,1,0,0]
Seq[5] = [1,1,0,0]
Seq[6] = [1,0,0,0]
Seq[7] = [1,0,0,1]

#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#GPIO.output(enable_pin, 1)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    print("forward")
    for i in range(steps):
        for j in range(StepCount):
            #print(i * j)
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
    setStep(0, 0, 0, 0)

def backwards(delay, steps):
    print("backward")
    for i in range(steps):
        for j in reversed(range(StepCount)):
            #print(i * j)
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
    setStep(0, 0, 0, 0)

#for test only
if __name__ == '__main__':
    while True:
        delay = raw_input("Zeitverzoegerung (ms)?")
        steps = raw_input("Wie viele Schritte vorwaerts? ")
        forward(int(delay) / 1000.0, int(steps))
        setStep(0,0,0,0)
        steps = raw_input("Wie viele Schritte rueckwaerts? ")
        backwards(int(delay) / 1000.0, int(steps))
        setStep(0,0,0,0)
