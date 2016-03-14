#Jérémy, Étienne
import time
from naoqi import ALProxy

IP = "192.168.0.15"
PORT = 9559
tempsVideo = 60

try:
    videoRecorderProxy = ALProxy("ALVideoRecorder", IP, PORT)
except Exception, e:
    print "Erreur"
    print str(e)
    exit(1)

videoRecorderProxy.setFrameRate(28.0)
videoRecorderProxy.setResolution(2)

videoRecorderProxy.startRecording("/home/nao/recordings/cameras", "dance")
print "Debut de lenregistrement"

time.sleep(tempsVideo)

videoInfo = videoRecorderProxy.stopRecording()
print "Dance Complete"