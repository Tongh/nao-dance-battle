#Raphael, Nicolas et Brian
import time
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "192.168.0.15", 9559)

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
