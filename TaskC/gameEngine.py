from random import randint
from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import csv
from recordData import RecordData

sense=SenseHat()
MAX_POINTS=30
bColour=(255,111,111)
tColour=(111,255,111)
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
        event = sense.stick.wait_for_event()
        intro="Player 1 and Player 2 take turns in rolling a die. The first one to roll {0} points is the winner. Let's start the game.".format(MAX_POINTS)
        sense.show_message(intro)
        sense.clear(bColour)
        sleep(1)

    def startGame(self):
        self.introToTheGame()
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
        
        sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")),text_colour=tColour)
        

    def setActivePlayerPointAndSwitchActivePlayer(self,points):
        activePlayerPoints=0
        
        for player in self.__playersList:
            if player.getActiveStatus():
                player.addPoints(points)
                activePlayerPoints = player.getPlayerInfo().get("points")
                sense.show_message("Points:{}".format(activePlayerPoints))
                if activePlayerPoints<MAX_POINTS:
                    sense.show_message("{}'s turn".format(player.getPlayerInfo().get("name")),text_colour=tColour)
                else:
                    self.__gameFinished = True
                    self.setWinner(player)
            player.setActiveStatus(not player.getActiveStatus())
            

    def gameFinished(self):
        self.gameEndTime = datetime.now().strftime("%H.%M.%S")
        sense.show_message("Winner:{}".format(self.getWinner().getPlayerInfo().get("name")),text_colour=tColour)
        sleep(1)
        sense.clear(bColour)
        self.recordData()
    
    def recordData(self):
        recData.writeTheRecord(self.getWinner(),self.gameEndTime)