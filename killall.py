import sys
from naoqi import ALProxy

def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    joint = joints
    rad = math.radians(angle)
    vitesse = speed
    id_action = motionProxy.post.changeAngles(joint, rad, vitesse)
    motionProxy.wait(id_action, 0)
	
ap = ALProxy("ALMotion", 192.168.0.15, 9559)
mouvement("Head", "HeadYaw", 31, 36)
