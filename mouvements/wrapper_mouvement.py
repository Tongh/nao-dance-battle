#Jason

from naoqi import ALProxy
import math


motionProxy = ALProxy("ALMotion", "192.168.0.15", 9559)

def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    rad = math.radians(angle)
    motionProxy.changeAngles(joints, rad, speed)