from naoqi import ALProxy
postureProxy = ALProxy("ALRobotPosture", "192.168.0.15", 9559)
postureProxy.goToPosture("Stand", 0.5)