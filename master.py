# -*- coding: utf-8 -*-
# Patrick

import sys
from naoqi import ALProxy
import math
import time
import threading


#--------------------------------------
#Variables
#--------------------------------------

robotIP = "127.0.0.1"
port = 9559
temps_choregraphie = 104

motionProxy = ALProxy("ALMotion", robotIP, port)
memoryProxy = ALProxy("ALMemory", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
tts = ALProxy("ALTextToSpeech", robotIP, port)
player = ALProxy("ALAudioPlayer", robotIP, port)
videoRecorderProxy = ALProxy("ALVideoRecorder", robotIP, port)

#--------------------------------------
#Méthodes générales
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
	postureProxy.goToPosture("Stand", 0.5)
	
def musique():
	tts.setVolume(1)	
	fileID = player.post.playFile("/home/nao/nao.mp3", 0.5, 1.0)
	print "Lecture de la musique en cours."
	time.sleep(temps_choregraphie)
	player.stopAll()

def chanter():
	time.sleep(43.25)
	tts.setParameter("pitchShift", 1)
	tts.setParameter("speed",90 )
	tts.say("\\vol=100\\Never gonna \\rspd=55\\ give you up. \\rspd=90\\ Never gonna \\rspd=55\\ let you \\rspd=60\\ down. \\rspd=90\\ Never gonna \\rspd=50\\ run around \\rspd=50\\ and. \\rspd=70\\ desert you")
	time.sleep(.3)
	tts.say("\\vol=100\\\\rspd=90\\ Never gonna \\rspd=70\\ make you \\emph=2\\ cry. \\rspd=90\\ Never gonna \\rspd=60\\ say \\emph=2\\\\rspd=80\\ good \\rspd=55\\ bye \\eos=1\\\\rspd=90\\ Never gonna \\rspd=60\\ tell \\rspd=70\\ a \\rspd=50\\ lie \\eos=1\\ \\rspd=60\\ and hurt \\rspd=60\\ you. ")
	time.sleep(25)
	tts.say("\\vol=100\\Never gonna \\rspd=55\\ give you up \\eos=1\\\\rspd=90\\ Never gonna \\rspd=55\\ let you \\rspd=50\\\\emph=2\\ down.\\rspd=90\\ Never gonna \\rspd=50\\ run around \\rspd=50\\ and. \\rspd=70\\ desert you")
	time.sleep(.3)
	tts.say("\\vol=100\\\\rspd=90\\ Never gonna \\rspd=70\\ make you cry. \\rspd=90\\ Never gonna \\rspd=60\\ say \\emph=2\\\\rspd=80\\ good \\rspd=55\\ bye \\vol=100\\\\eos=1\\\\rspd=90\\ Never gonna \\rspd=60\\ tell \\rspd=70\\ a \\rspd=50\\ lie \\eos=1\\ \\rspd=60\\ and hurt \\rspd=60\\ you. ")
		
#--------------------------------------	
#Chorégraphie	
#--------------------------------------

LHand = 0.00
tts.say("Press my head!")

while (LHand == 0.00):
	LHand = memoryProxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
print "Début de la chorégraphie."

#--------------------------------------

postureProxy.goToPosture("Stand", 0.5)
tts.say("Get ready to dance!")
time.sleep(3)

#--------------------------------------

thread_video = threading.Thread(None, filmer, None)
thread_video.start()

thread_musique = threading.Thread(None, musique, None)
thread_musique.start()

thread_chanter = threading.Thread(None, chanter, None)
thread_chanter.start()

#--------------------------------------

def move_un():
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

move_un()

#--------------------------------------

def move_deux():
	postureProxy.goToPosture("StandZero", 0.5)
	time.sleep(1)
	postureProxy.goToPosture("Crouch", 0.8)
	time.sleep(2)
	postureProxy.goToPosture("StandZero", 0.5)
	time.sleep(2)
	mouvement("LLeg", "LHipRoll", -2, 0.1)
	mouvement("LLeg", "LAnkleRoll", 2, 0.1)
	mouvement("RLeg", "RHipRoll", -12, 0.1)
	time.sleep(2)
	mouvement("LLeg", "LHipRoll", 12, 0.1)
	mouvement("RLeg", "RKneePitch", 5, 0.1)
	mouvement("RLeg", "RHipRoll", 12, 0.1)
	mouvement("RLeg", "RAnkleRoll", -2, 0.1)
	time.sleep(1)
	postureProxy.goToPosture("Stand", 0.5)
	time.sleep(1)

move_deux()

#--------------------------------------

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

def move_trois():
	a = threading.Thread(None, mouvementbrasdroit, None)
	b = threading.Thread(None, mouvementbrasgauche, None)
 
	postureProxy.goToPosture("StandZero", 0.8)
	time.sleep(1)
 
	mouvement("RArm", "RElbowYaw", 50, 0.5)
	mouvement("LArm", "LElbowYaw", -50, 0.5)
 
	a.start()
	b.start()

	time.sleep(5)

move_trois()

#--------------------------------------

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

tete()
postureProxy.goToPosture("Stand", 0.5)	
time.sleep(1)

#--------------------------------------

def bras():
	for i in range(7):
		mouvement("LArm", "LElbowYaw", 50, 0.4)
		mouvement("RArm", "RShoulderRoll", -76, 0.4)
		time.sleep(0.4)
		mouvement("LArm", "LElbowYaw", -50, 0.4)
		mouvement("RArm", "RShoulderRoll", 76, 0.4)
		time.sleep(0.4)

thread_bras = threading.Thread(None, bras, None)
thread_bras.start()
tete()
time.sleep(1)

#--------------------------------------

def mouvementCheville():
	mouvement("LLeg", "LAnklePitch", -68, 0.1)
	mouvement("RLeg", "RAnklePitch", -68, 0.1)
	time.sleep(1)

def mouvementGenou():
	mouvement("LLeg", "LKneePitch", 121, 0.2)
	mouvement("RLeg", "RKneePitch", 121, 0.2)
	time.sleep(1)

def penche():
	mouvement("RLeg", "RHipPitch", -40, 0.1)
	mouvement("LLeg", "LHipPitch", -40, 0.1)
	time.sleep(1)

def pencheAvant():
	mouvement("RLeg", "RHipPitch", -30, 0.1)
	mouvement("LLeg", "LHipPitch", -30, 0.1)
	time.sleep(1)

def leverBras():
	mouvement("RArm", "RShoulderPitch", 121, 0.1)
	mouvement("LArm", "LShoulderPitch", -121, 0.1)
	time.sleep(1)

def fermerMainGauche():
    motionProxy.closeHand("LHand")

thread_penche = threading.Thread(None, penche, None)
thread_penche.start()

thread_mouvementCheville = threading.Thread(None, mouvementCheville, None)
#thread_mouvementCheville.start()

thread_mouvementGenou = threading.Thread(None, mouvementGenou, None)
#thread_mouvementGenou.start()

thread_leverBras = threading.Thread(None, leverBras, None)
thread_leverBras.start()

thread_fermerMainGauche = threading.Thread(None, fermerMainGauche, None)
thread_fermerMainGauche.start()

motionProxy.closeHand("RHand")

time.sleep(1)
mouvement("Head", "HeadPitch", -38, 0.1)
motionProxy.openHand("LHand")
time.sleep(2)
postureProxy.goToPosture("Stand", 0.5)	
time.sleep(3)

#--------------------------------------

mouvement("LArm", "LElbowYaw", -85, 0.6)
mouvement("LArm", "LElbowRoll", -40,0.6)
mouvement("LArm", "LShoulderRoll", -40,0.6)
mouvement("RArm", "RShoulderRoll", -40,0.6)
mouvement("Head", "HeadPitch", 10, 0.6)
mouvement("Head", "HeadYaw", -13, 0.6)
time.sleep(1)
mouvement("LArm", "LWristYaw", 40,0.6)
mouvement("LArm", "LElbowRoll", 40,0.6)
mouvement("LArm", "LShoulderRoll", 40,0.6)
mouvement("RArm", "RWristYaw", -40,0.6)
mouvement("RArm", "RShoulderRoll", -40,0.6)
mouvement("Head", "HeadPitch", 10,0.5)
mouvement("Head", "HeadYaw", 5,0.5)
time.sleep(1)
mouvement("LArm", "LShoulderPitch", -40,0.6)
mouvement("LArm", "LElbowYaw", -40,0.6)
mouvement("LArm", "LShoulderRoll", -40,0.6)
mouvement("RArm", "RShoulderPitch", 40,0.6)
mouvement("RArm", "RShoulderRoll", 40,0.6)
mouvement("Head", "HeadPitch", -5,0.5)
mouvement("Head", "HeadYaw", 10,0.5)
time.sleep(1)
mouvement("LArm", "LShoulderPitch", -40,0.6)
mouvement("LArm", "LWristYaw",40,0.6)
mouvement("LArm", "LShoulderRoll", 40,0.6)
mouvement("RArm", "RShoulderPitch", -40,0.6)
mouvement("RArm", "RWristYaw",-40,0.6)
mouvement("RArm", "RShoulderRoll", -40,0.6)
mouvement("Head", "HeadYaw", 10,0.5)
mouvement("Head", "HeadPitch", 10,0.5)
time.sleep(1)
postureProxy.goToPosture("Stand", 0.5)	
time.sleep(1)

#--------------------------------------

move_trois()
tete()
move_un()

import atexit
atexit.register(fermer)