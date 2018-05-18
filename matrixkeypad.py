import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

D2 = 17
D3 = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
D8 = 25
D9 = 4
D10 = 8
A3 = 7

MATRIX = [[1,2,3,'A'],
          [4,5,6,'B'],
          [7,8,9,'C'],
          ['*',0,'#','D']]
           
ROW = [D9, D8, D7, D6]
COL = [D5, D4, D3, D2]

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

def checkKeypress():
    for j in range(4):
        GPIO.output(COL[j],0)
        for i in range(4):
            if GPIO.input(ROW[i])==0:
                GPIO.output(COL[j],1)
                return MATRIX[i][j]
                #time.sleep(0.2)
                #while GPIO.input(ROW[i])==0:
                    #pass
        GPIO.output(COL[j],1)
        
