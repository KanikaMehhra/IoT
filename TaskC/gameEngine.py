from random import randint
from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import csv
import modules
import constants

sense=SenseHat()

class GameEngine:
    def __init__(self,die):
        super().__init__()
        self.__playersList=[]
        self.__winner=None
        self.__die=die
        self.firstPlayerIsActive=True
        self.gameEndTime=""

    def addPlayer(self, player):
        self.__playersList.append(player)

    #welcome and introduction section at the start of the game
    def introToTheGame(self):
        welcome = "Welcome to the electronic die game. Press the joystick to go through the game's instructions."
        sense.show_message(welcome,scroll_speed=0)
        sense.stick.wait_for_event()
        intro="Player 1 and Player 2 take turns in rolling a die. The first one to roll {0} points is the winner. Let's start the game.".format(constants.MAX_POINTS)
        sense.show_message(intro,scroll_speed=0)
        sense.clear(constants.B_COLOUR)
        sleep(1)

    #starts the game engine
    def startGame(self):
        self.introToTheGame()
        self.setInitialActivePlayerStatus()
        while self.__playersList[0].getPlayerInfo().get("points")<constants.MAX_POINTS and self.__playersList[1].getPlayerInfo().get("points")<constants.MAX_POINTS:
            self.__die.listenForShake() 
            self.setActivePlayerPointAndSwitchActivePlayer(self.__die.getFaceValue())    

    #set initial players' active status.
    def setInitialActivePlayerStatus(self):
       self.__playersList[0].setActiveStatus(True)
       sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
       self.__playersList[1].setActiveStatus(False)

    #change the active player status and assigns the respective points to the respective player.
    def setActivePlayerPointAndSwitchActivePlayer(self,points):
        activePlayerPoints=0
        #if player 1 is active, add the points to player 1 bucket.
        if self.__playersList[0].getActiveStatus():
            self.__playersList[0].addPoints(points)
            activePlayerPoints=self.__playersList[0].getPlayerInfo().get("points")
            sense.show_message("Points:{}".format(activePlayerPoints))
            if activePlayerPoints<constants.MAX_POINTS:
                sense.show_message("{}'s turn".format(self.__playersList[1].getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
            else:
                self.__winner=self.__playersList[0]
        #else if player 2 is active, add the points to player 2 bucket.
        else:   
            self.__playersList[1].addPoints(points)
            activePlayerPoints=self.__playersList[1].getPlayerInfo().get("points")
            sense.show_message("Points:{}".format(activePlayerPoints))
            if activePlayerPoints<constants.MAX_POINTS:
                sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
            else:
                self.__winner=self.__playersList[1]

        #switching the active player status.
        self.__playersList[0].setActiveStatus(not self.__playersList[0].getActiveStatus())
        self.__playersList[1].setActiveStatus(not self.__playersList[1].getActiveStatus())

    #ends the game engine.
    def gameFinished(self):
        self.gameEndTime = datetime.now().strftime("%H.%M.%S")
        sense.show_message("Winner:{}".format(self.__winner.getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
        sleep(1)
        sense.clear(constants.B_COLOUR)
        self.recordData()
    
    #records data to the csv file.
    def recordData(self):
        modules.writeTheRecord(self.__winner,self.gameEndTime)






