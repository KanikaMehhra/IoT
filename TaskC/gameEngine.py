from random import randint
from sense_hat import SenseHat
from time import sleep
from datetime import datetime
from recordData import RecordData

import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 
import constants

sense=SenseHat()
recData=RecordData()

class GameEngine:
    def __init__(self,die):
        super().__init__()
        self.__playersList=[]
        self.__winner=None
        self.__die=die
        self.__gameFinished = False
        self.firstPlayerIsActive=True
        self.gameEndTime=""

    def addPlayer(self, player):
        self.__playersList.append(player)

    def setWinner(self,winnerPlayer):
        self.__winner=winnerPlayer

    def getWinner(self):
        return self.__winner

    def introToTheGame(self):
        welcome = "Welcome to the electronic die game. Press the joystick to go through the game's instructions."
        sense.show_message(welcome)
        sense.stick.wait_for_event()
        intro="Player 1 and Player 2 take turns in rolling a die. The first one to roll {0} points is the winner. Let's start the game.".format(constants.MAX_POINTS)
        sense.show_message(intro)
        sense.clear(constants.B_COLOUR)
        sleep(1)

    def startGame(self):
        #self.introToTheGame()
        self.setInitialActivePlayerStatus()
        while not self.__gameFinished:
            value = self.__die.listenForShake()
            if value != 0:
                self.setActivePlayerPointAndSwitchActivePlayer(self.__die.getFaceValue())

    def setInitialActivePlayerStatus(self):
#TODO does it matter if the message is displayed after the loop?
        index = 0
        for player in self.__playersList:
            if index == 0:
                player.setActiveStatus(True)
            else: 
                player.setActiveStatus(False)
            index += 1
        
        sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
        

    def setActivePlayerPointAndSwitchActivePlayer(self,points):
        activePlayerPoints=0
        
        i = 0
        for player in self.__playersList:
            if player.getActiveStatus():
                player.addPoints(points)
                activePlayerPoints = player.getPlayerInfo().get("points")
                sense.show_message("Points:{}".format(activePlayerPoints))
                if activePlayerPoints < constants.MAX_POINTS:
                    if i == len(self.__playersList) - 1:
                        nextI = 0
                    else:
                        nextI = i + 1
                    sense.show_message("{}'s turn".format(self.__playersList[nextI].getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
                else:
                    self.__gameFinished = True
                    self.setWinner(player)
            i += 1
            player.setActiveStatus(not player.getActiveStatus())
            

    def gameFinished(self):
        self.gameEndTime = datetime.now().strftime("%H.%M.%S")
        sense.show_message("Winner:{}".format(self.getWinner().getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
        sleep(1)
        sense.clear(constants.B_COLOUR)
        self.recordData()
    
    def recordData(self):
        recData.writeTheRecord(self.getWinner(),self.gameEndTime)