from random import randint
from sense_hat import SenseHat
from time import sleep
from datetime import datetime

import modules
import constants
from playerLinkedList import PlayerLinkedList


sense=SenseHat()

class GameEngine:
    def __init__(self,die):
        super().__init__()
        self.__playersList=PlayerLinkedList()
        self.__winner=None
        self.__die=die
        self.__gameEndTime=""


    def addPlayer(self, player):
        self.__playersList.insert(player)

    #welcome and introduction section at the start of the game
    def introToTheGame(self):
        welcome = "Welcome to the electronic die game. Press the joystick to go through the game's instructions."
        sense.show_message(welcome)
        sense.stick.wait_for_event()
        intro="Player 1 and Player 2 take turns in rolling a die. The first one to roll {0} points is the winner. Let's start the game.".format(constants.MAX_POINTS)
        sense.show_message(intro)
        sense.clear(constants.B_COLOUR)
        sleep(1)

    #starts the game engine
    def startGame(self):
        self.introToTheGame()
        self.setInitialActivePlayerStatus()
         while self.__winner == None:
             self.__die.listenForShake() 
             self.setActivePlayerPointAndSwitchActivePlayer(self.__die.getFaceValue())   

    #set initial players' active status.
    def setInitialActivePlayerStatus(self):
        self.__playersList.getHead().getData().setActiveStatus(True)
        sense.show_message("{}'s turn".format(self.__playersList.getHead().getData().getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)

    #change the active player status and assigns the respective points to the respective player.
    def setActivePlayerPointAndSwitchActivePlayer(self,points):
        activePlayerNode=self.__playersList.getActivePlayerNode()
        activePlayerNode.getData().addPoints(points)
        activePlayerPoints=activePlayerNode.getData().getPlayerInfo().get("points")
        sense.show_message("Points:{}".format(activePlayerPoints))

        if activePlayerPoints<constants.MAX_POINTS:
            activePlayerNode.getData().setActiveStatus(False)
            activePlayerNode.getNext().getData().setActiveStatus(True)
            sense.show_message("{}'s turn".format(activePlayerNode.getNext().getData().getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
        else:
            self.__winner=activePlayerNode.getData()

    #ends the game engine.
    def gameFinished(self):
        self.__gameEndTime = datetime.now().strftime("%H.%M.%S")
        sense.show_message("Winner:{}".format(self.__winner.getPlayerInfo().get("name")),text_colour=constants.T_COLOUR)
        sleep(1)
        sense.clear(constants.B_COLOUR)
        self.recordData()
    
    #records data to the csv file.
    def recordData(self):
        modules.writeTheRecord(self.__winner,self.__gameEndTime)






