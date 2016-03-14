from naoqi import ALProxy
robotIP = "192.168.0.15"
port = 9559
player = ALProxy("ALAudioPlayer", robotIP, port)
player.stopAll()