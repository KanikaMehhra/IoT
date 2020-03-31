import modules 
from random import randint
from sense_hat import SenseHat
from electronicDie import electronicDie
from time import sleep

sense=SenseHat()

MAX_POINTS=30
firstPlayerIsActive=True

class gameEngine:
    def __init__(self,die):
        super().__init__()
        self.__playersList=[]
        self.__winner=None
        self.__die=die
        self.firstPlayerIsActive=True

    def addPlayer(self, player):
        self.__playersList.append(player)

    def setWinner(self,winnerPlayer):
        self.__winner=winnerPlayer

    def getWinner(self):
        return self.__winner

    def introToTheGame(self):
        welcome = "Welcome to the electronic die game. Press the joystick to go through the game's instructions."
        sense.show_message(welcome, scroll_speed=0)
        bColour=(255,111,111)
        event = sense.stick.wait_for_event()

        intro="Player 1 and Player 2 take turns in rolling a die. The first one to roll {0} points is the winner. Press joystick while switching between the players. Let's start the game".format(MAX_POINTS)
        sense.show_message(intro, scroll_speed=0)
        sense.clear(bColour)
        sleep(1)

    def startGame(self):
        self.introToTheGame()
        sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")))
        print("SAT INITIAL")
        while self.__playersList[0].getPlayerInfo().get("points")<MAX_POINTS and self.__playersList[1].getPlayerInfo().get("points")<MAX_POINTS:
            self.__die.listenForShake() 
            print("SHOOK")
            self.setActivePlayerPointAndSwitchActivePlayer(self.__die.getFaceValue())
            
        

    #def setInitialActivePlayerStatus(self):
     #   self.__playersList[0].setActiveStatus(True)
      #  sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")))
       # self.__playersList[1].setActiveStatus(False)
        #print("1={}".format( self.__playersList[0].getActiveStatus()))
        #print("2={}".format( self.__playersList[1].getActiveStatus()))


    def setActivePlayerPointAndSwitchActivePlayer(self,points):
        if self.firstPlayerIsActive:
            self.__playersList[0].addPoints(points)
            sense.show_message("Points:{}".format(self.__playersList[0].getPlayerInfo().get("points")))
            sense.show_message("{}'s turn".format(self.__playersList[1].getPlayerInfo().get("name")))
        else:
            self.__playersList[1].addPoints(points)
            sense.show_message("Points:{}".format(self.__playersList[1].getPlayerInfo().get("points")))
            sense.show_message("{}'s turn".format(self.__playersList[0].getPlayerInfo().get("name")))

        self.firstPlayerIsActive=not self.firstPlayerIsActive
        #self.__playersList[0].setActiveStatus(not self.__playersList[0].getActiveStatus())
        #self.__playersList[1].setActiveStatus(not self.__playersList[1].getActiveStatus())






