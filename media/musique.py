import time
from naoqi import ALProxy

voix = ALProxy("ALTextToSpeech", "192.168.0.15", 9559)
voix.setVolume(1)
player = ALProxy("ALAudioPlayer", "192.168.0.15", 9559)
fileID = player.post.playFile("/home/nao/nao.wav", 0.5, 1.0)
print "play music!"
time.sleep(60)
player.stopAll()