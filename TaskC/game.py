import random
import modules 
from random import randint
from ElectronicDie import electronicDie

initOrientationTuple=modules.getCurrentAccelerationTuple()
die=electronicDie(randint(1,6), initOrientationTuple)

die.listenForShake()