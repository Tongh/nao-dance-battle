#Patrick

import sys
from naoqi import ALProxy
import math
import time
import threading


motionProxy = ALProxy("ALMotion", "192.168.0.15", 9559)

def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    rad = math.radians(angle)
    motionProxy.changeAngles(joints, rad, speed)
	
def head_tilt_super_cool():
	for i in range(2):
		mouvement("Head", "HeadPitch", 25, 0.5)
		time.sleep(0.3)
		mouvement("Head", "HeadPitch", -25, 0.5)
		time.sleep(0.3)

angles = [70, -70, -70, 70]

def tete():
	for i in range(4):		
		mouvement("Head", "HeadYaw", angles[i], 0.8)
		time.sleep(1)
		head_tilt_super_cool()

def bras():
	for i in range(9):
		mouvement("LArm", "LElbowYaw", 50, 0.4)
		mouvement("RArm", "RShoulderRoll", -76, 0.4)
		time.sleep(0.4)
		mouvement("LArm", "LElbowYaw", -50, 0.4)
		mouvement("RArm", "RShoulderRoll", 76, 0.4)
		time.sleep(0.4)

def jambes():
	for i in range(9):
		mouvement("LLeg", "LHipPitch", 20, 0.4)
		mouvement("RLeg", "RHipPitch", -20, 0.4)
		time.sleep(0.4)
		mouvement("LLeg", "LHipPitch", -20, 0.4)
		mouvement("RLeg", "RHipPitch", 20, 0.4)
		time.sleep(0.4)
			
a = threading.Thread(None, tete, None)
a.start()
b = threading.Thread(None, bras, None)
b.start()
