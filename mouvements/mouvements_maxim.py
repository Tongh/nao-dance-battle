from naoqi import ALProxy
import math
import time
import threading
 
 
motionProxy = ALProxy("ALMotion", "192.168.0.15", 9559)
talk = ALProxy("ALTextToSpeech", "192.168.0.15", 9559)
posture = ALProxy("ALRobotPosture", "192.168.0.15", 9559)
 
#Maxim Isabel
 
def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    joint = joints
    rad = math.radians(angle)
    vitesse = speed
    motionProxy.changeAngles(joint, rad, vitesse)
 
def mouvementbrasdroit():
    mouvement("RArm", "RShoulderPitch", -50, 0.5)
    time.sleep(1)
    for x in xrange(0, 5):
        mouvement("RArm", "RShoulderPitch", 100, 0.5)
        time.sleep(1)
        mouvement("RArm", "RShoulderPitch", -100, 0.5)
        time.sleep(1)
 
def mouvementbrasgauche():
    mouvement("LArm", "LShoulderPitch", 50, 0.5)
    time.sleep(1)
    for x in xrange(0, 5):
        mouvement("LArm", "LShoulderPitch", -100, 0.5)
        time.sleep(1)
        mouvement("LArm", "LShoulderPitch", 100, 0.5)
        time.sleep(1)
 
a = threading.Thread(None, mouvementbrasdroit, None)
b = threading.Thread(None, mouvementbrasgauche, None)
 
 
posture.goToPosture("StandZero", 0.8)
time.sleep(1)
 
mouvement("RArm", "RElbowYaw", 50, 0.5)
mouvement("LArm", "LElbowYaw", -50, 0.5)
 
a.start()
b.start()