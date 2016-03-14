from naoqi import ALProxy
import math
import time

motionProxy = ALProxy("ALMotion", "192.168.0.15", 9559)
talk = ALProxy("ALTextToSpeech", "192.168.0.15", 9559)
posture = ALProxy("ALRobotPosture", "192.168.0.15", 9559)


def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    joint = joints
    rad = math.radians(angle)
    vitesse = speed
    id_action = motionProxy.post.changeAngles(joint, rad, vitesse)
    motionProxy.wait(id_action, 0)

#Christian
posture.goToPosture("StandZero", 0.5)
time.sleep(2)
mouvement("Head", "HeadPitch", -59, 0.3)
mouvement("LArm", "LShoulderRoll", 77, 0.3)
mouvement("RArm", "RShoulderRoll", -76, 0.3)
time.sleep(2)
mouvement("Head", "HeadPitch", 88.5, 0.3)
mouvement("Head", "HeadYaw", -80, 0.3)
mouvement("LArm", "LElbowRoll", -88.5, 0.3)
time.sleep(2)
posture.goToPosture("Stand",0.3)
time.sleep(1)

#Alexandre
posture.goToPosture("StandZero", 0.5)
time.sleep(1)
posture.goToPosture("Crouch", 0.8)
time.sleep(2)
posture.goToPosture("StandZero", 0.5)
time.sleep(2)
mouvement("LLeg", "LHipRoll", -10, 0.1)
mouvement("LLeg", "LAnkleRoll", 10, 0.1)
mouvement("RLeg", "RHipRoll", -30, 0.1)
time.sleep(2)
mouvement("LLeg", "LHipRoll", 40, 0.1)
mouvement("LLeg", "LAnkleRoll", -10, 0.1)
mouvement("RLeg", "RKneePRoll", 25, 0.1)
mouvement("RLeg", "RHipRoll", 40, 0.1)
mouvement("RLeg", "RAnkleRoll", -10, 0.1)
time.sleep(1)
mouvement("LLeg", "LHipPitch", -15, 0.06)
mouvement("RLeg", "RHipPitch", -15, 0.06)
mouvement("RLeg", "RAnklePitch", 15, 0.06)