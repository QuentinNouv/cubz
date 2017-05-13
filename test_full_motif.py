import RPi.GPIO as GPIO
import time
from Motifs import *
dimCube = 3
ledPCou = 9
#tpsAffCou = 1000 # 1 en seconde ?
vitesseMAJ = 0.100
low = GPIO.LOW
high = GPIO.HIGH
Ano = [26,20,21,16,19,13,12,6,5]
Cat = [17,18,27]

def main():
    setup_gpio()
    animation(mon_motif)

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for i in Ano:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,low)
    for i in Cat:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,high)

def gp_state_swap(id, state):
    if state == 0:
        GPIO.output(id, low)
    else:
        GPIO.output(id, high)

def animation(motif):
    xTabMot = 0
    xled = 0
    for current_motif in motif:
        indAff_cou = current_motif[-1]
        tempsFin = time.clock() + (indAff_cou * vitesseMAJ)
        while tempsFin > time.clock():
            xTabMot = 0
            for couche in range(dimCube):
                if couche == 0:
                    GPIO.output(Cat[dimCube-1], high)
                else:
                    GPIO.output(Cat[couche - 1], high)
                xled = 0
                for ligLed in range(dimCube):
                    for colLed in range(dimCube):
                        gp_state_swap(Ano[xled],(current_motif[xTabMot] & (1 << colLed)))
                        xled += 1
                    xTabMot += 1
                gp_state_swap(Cat[couche],low)
                time.sleep(0.001)
