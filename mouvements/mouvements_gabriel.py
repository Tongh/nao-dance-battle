# Gabriel
import math
import sys
import time
import random
from naoqi import ALProxy
motionProxy = ALProxy("ALMotion", "192.168.0.15", 9559)

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    joint = joints
    rad = math.radians(angle)
    vitesse = speed
    id_action = motionProxy.post.changeAngles(joint, rad, vitesse)
    motionProxy.wait(id_action, 0)


    # Init proxies.
postureProxy = ALProxy("ALRobotPosture", "192.168.0.15", 9559)
postureProxy.goToPosture("StandZero", 0.5)
time.sleep(1)
mouvement("LArm", "LElbowYaw", -85, 1.0)
mouvement("LArm", "LElbowRoll", -1.5,1.0)
mouvement("LArm", "LShoulderRoll", -1.5,1.0)
mouvement("RArm", "RShoulderRoll", -1.5,1.0)
mouvement("Head", "HeadPitch", 10, 1.0)
mouvement("Head", "HeadYaw", -13, 1.0)
time.sleep(1)
mouvement("LArm", "LWristYaw", 1.5,1.0)
mouvement("LArm", "LElbowRoll", 1.5,1.0)
mouvement("LArm", "LShoulderRoll", 1.5,1.0)
mouvement("RArm", "RWristYaw", -1.5,1.0)
mouvement("RArm", "RShoulderRoll", -1.5,1.0)
mouvement("Head", "HeadPitch", 10,0.5)
mouvement("Head", "HeadYaw", 5,0.5)
time.sleep(1)
mouvement("LArm", "LShoulderPitch", -1.5,1.0)
mouvement("LArm", "LElbowYaw", -1.5,1.0)
mouvement("LArm", "LShoulderRoll", -1.5,1.0)
mouvement("RArm", "RShoulderPitch", 1.5,1.0)
mouvement("RArm", "RShoulderRoll", 1.5,1.0)
mouvement("Head", "HeadPitch", -5,0.5)
mouvement("Head", "HeadYaw", 10,0.5)
time.sleep(1)
mouvement("LArm", "LShoulderPitch", -1.5,1.0)
mouvement("LArm", "LWristYaw",1.5,1.0)
mouvement("LArm", "LShoulderRoll", 1.5,1.0)
mouvement("RArm", "RShoulderPitch", -1.5,1.0)
mouvement("RArm", "RWristYaw",-1.5,1.0)
mouvement("RArm", "RShoulderRoll", -1.5,1.0)
mouvement("Head", "HeadYaw", 0,0.5)
mouvement("Head", "HeadPitch", 0,0.5)
time.sleep(1)


time.sleep(1)

