#Programmé par Tommy Rochefort

from naoqi import ALProxy
robotIP = "192.168.0.15"
memoryProxy = ALProxy("ALMemory", robotIP, 9559)
postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
RHand = 0.00

while (RHand == 0.00):
	RHand = memoryProxy.getData("Device/SubDeviceList/RHand/Touch/Back/Sensor/Value	")

#code suivant