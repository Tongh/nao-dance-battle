# Les mouvements
def mouvementCheville():
    mouvement("LLeg", "LAnklePitch", -68, 0.1)

def mouvementCheville2():
    mouvement("RLeg", "RAnklePitch", -68, 0.1)

def mouvementGenou():
    mouvement("LLeg", "LKneePitch", 121, 0.2)

def mouvementGenou2():
    mouvement("RLeg", "RKneePitch", 121, 0.2)

def penche():
    mouvement("RLeg", "RHipPitch", -40, 0.1)
    mouvement("LLeg", "LHipPitch", -40, 0.1)

def pencheAvant():
    mouvement("RLeg", "RHipPitch", -30, 0.1)
    mouvement("LLeg", "LHipPitch", -30, 0.1)

def leverBras():
    mouvement("RArm", "RShoulderPitch", 121, 0.1)
    mouvement("LArm", "LShoulderPitch", -121, 0.1)

def fermerMainGauche():
    motionProxy.closeHand("LHand")


penche()
mouvementCheville()
mouvementCheville2()
mouvementGenou()
mouvementGenou2()
leverBras()
a = threading.Thread(None, fermerMainGauche, None)
motionProxy.closeHand("RHand")
time.sleep(1)
mouvement("Head", "HeadPitch", -38, 0.1)
motionProxy.openHand("LHand")
time.sleep(2)
pencheAvant()