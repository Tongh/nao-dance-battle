import sys 
import os
from naoqi import ALProxy	
from media import musique, camera

scriptpath = "../sensors/sensors.py"
sys.path.append(os.path.abspath(scriptpath))
import sensors

print "test! it works"
x = raw_input()