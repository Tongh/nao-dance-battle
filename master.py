# -*- coding: utf-8 -*-
#Patrick

import sys
from naoqi import ALProxy
import math
import time
import threading


#--------------------------------------
#Variables
#--------------------------------------

robotIP = "192.168.0.15"
port = 9559
temps_choregraphie = 90

motionProxy = ALProxy("ALMotion", robotIP, port)
memoryProxy = ALProxy("ALMemory", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
tts = ALProxy("ALTextToSpeech", robotIP, port)
player = ALProxy("ALAudioPlayer", robotIP, port)
videoRecorderProxy = ALProxy("ALVideoRecorder", robotIP, port)

#--------------------------------------
#Methodes
#--------------------------------------   
 
def mouvement(part, joints, angle, speed):
    motionProxy.setStiffnesses(part, 1.0)
    rad = math.radians(angle)
    motionProxy.changeAngles(joints, rad, speed)

def filmer():
	if videoRecorderProxy.isRecording():
		videoRecorderProxy.stopRecording()
		
	videoRecorderProxy.setFrameRate(28.0)
	videoRecorderProxy.setResolution(2)

	videoRecorderProxy.startRecording("/home/nao/recordings/cameras", "dance")
	print "Début de l'enregistrement"

	time.sleep(temps_choregraphie)

	videoInfo = videoRecorderProxy.stopRecording()
	print "Enregistrement complété!"

def fermer():
	if videoRecorderProxy.isRecording():
		videoRecorderProxy.stopRecording()
	player.stopAll()
	
def musique():
	tts.setVolume(1)	
	fileID = player.post.playFile("/home/nao/nao.mp3", 0.5, 1.0)
	print "Lecture de la musique en cours."
	time.sleep(temps_choregraphie)
	player.stopAll()

def chanter():
	time.sleep(42)
	tts.setParameter("pitchShift", 1)
	tts.setParameter("speed",90 )
	tts.say("\\vol=100\\Never gonna \\rspd=55\\ give you up. \\rspd=90\\ Never gonna \\rspd=55\\ let you \\rspd=60\\ down. \\rspd=90\\ Never gonna \\rspd=50\\ run around \\rspd=50\\ and. \\rspd=70\\ desert you")
	time.sleep(.3)
	tts.say("\\vol=100\\\\rspd=90\\ Never gonna \\rspd=70\\ make you \\emph=2\\ cry. \\rspd=90\\ Never gonna \\rspd=60\\ say \\emph=2\\\\rspd=80\\ good \\rspd=55\\ bye \\eos=1\\\\rspd=90\\ Never gonna \\rspd=60\\ tell \\rspd=70\\ a \\rspd=50\\ lie \\eos=1\\ \\rspd=60\\ and hurt \\rspd=60\\ you. ")
	#time.sleep(24)
	#tts.say("\\vol=100\\Never gonna \\rspd=55\\ give you up \\eos=1\\\\rspd=90\\ Never gonna \\rspd=55\\ let you \\rspd=50\\\\emph=2\\ down.\\rspd=90\\ Never gonna \\rspd=50\\ run around \\rspd=50\\ and. \\rspd=70\\ desert you")
	#time.sleep(.3)
	#tts.say("\\vol=100\\\\rspd=90\\ Never gonna \\rspd=70\\ make you cry. \\rspd=90\\ Never gonna \\rspd=60\\ say \\emph=2\\\\rspd=80\\ good \\rspd=55\\ bye \\vol=100\\\\eos=1\\\\rspd=90\\ Never gonna \\rspd=60\\ tell \\rspd=70\\ a \\rspd=50\\ lie \\eos=1\\ \\rspd=60\\ and hurt \\rspd=60\\ you. ")

#--------------------------------------	
#Choregraphie	
#--------------------------------------

RHand = 0.00

while (RHand == 0.00):
	RHand = memoryProxy.getData("Device/SubDeviceList/LHand/Touch/Back/Sensor/Value")
print "Début de la chorégraphie."

#--------------------------------------

postureProxy.goToPosture("Stand", 0.5)
tts.say("Get ready to dance!")
time.sleep(5)

#--------------------------------------

thread_video = threading.Thread(None, filmer, None)
thread_video.start()

thread_musique = threading.Thread(None, musique, None)
thread_musique.start()

thread_chanter = threading.Thread(None, chanter, None)
thread_chanter.start()

#--------------------------------------

postureProxy.goToPosture("StandZero", 0.5)
time.sleep(2)
mouvement("Head", "HeadPitch", -59, 0.3)
mouvement("LArm", "LShoulderRoll", 77, 0.3)
mouvement("RArm", "RShoulderRoll", -76, 0.3)
time.sleep(2)
mouvement("Head", "HeadPitch", 88.5, 0.3)
mouvement("Head", "HeadYaw", -80, 0.3)
mouvement("LArm", "LElbowRoll", -88.5, 0.3)
time.sleep(2)
postureProxy.goToPosture("Stand",0.3)
time.sleep(1)

#--------------------------------------

postureProxy.goToPosture("StandZero", 0.5)
time.sleep(1)
postureProxy.goToPosture("Crouch", 0.8)
time.sleep(2)
postureProxy.goToPosture("StandZero", 0.5)
time.sleep(2)
mouvement("LLeg", "LHipRoll", -10, 0.1)
mouvement("LLeg", "LAnkleRoll", 10, 0.1)
mouvement("RLeg", "RHipRoll", -30, 0.1)
time.sleep(2)
mouvement("LLeg", "LHipRoll", 40, 0.1)
mouvement("LLeg", "LAnkleRoll", -10, 0.1)
mouvement("RLeg", "RKneePitch", 25, 0.1)
mouvement("RLeg", "RHipRoll", 40, 0.1)
mouvement("RLeg", "RAnkleRoll", -10, 0.1)
time.sleep(1)
mouvement("LLeg", "LHipPitch", -15, 0.06)
mouvement("RLeg", "RHipPitch", -15, 0.06)
mouvement("RLeg", "RAnklePitch", 15, 0.06)

#--------------------------------------

import atexit
atexit.register(fermer)