import sys
from naoqi import ALProxy


ap = ALProxy("ALMotion", 192.168.0.15, 9559)
ap.killAll()
