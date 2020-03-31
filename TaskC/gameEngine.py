import random
import modules 
from random import randint
from sense_hat import SenseHat
sense=SenseHat()

MAX_POINTS=30
class gameEngine:
    def __init__(self):
        super().__init__()
        self.__playersList=[]
        self.__winner=None

    def addPlayer(self, player):
        self.__playersList.append(player)

    def setWinner(self,winnerPlayer):
        self.__winner=winnerPlayer

    def getWinner(self):
        return self.__winner

    def startGame(self):
        intro = "Welcome to the electronic die game. Press the joystick to go through the game's instructions."
        sense.show_message(intro, scroll_speed=0)
        bColour=(255,111,111)
        sense.show_message("Press joystick", back_colour=bColour)
        
        messages=["Player 1 and Player 2 take turns in rolling a die.",
        " The first one to roll {0} points is the winner".format(MAX_POINTS),
        "press joystick while switching between the players",
        "Let's start the game"]

        for line in range (0,len(messages)):
            event = sense.stick.wait_for_event()
            sense.show_message(messages[line])
            sense.show_message("Press joystick", back_colour=bColour)
