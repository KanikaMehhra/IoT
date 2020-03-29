from player import Player
from electronicDie import ElectronicDie
from sense_hat import SenseHat
from recordData import RecordData
from datetime import datetime

import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 
import constants

class GameEngine():
    def __init__(self):
        self.__sense = SenseHat()
        self.__player1 = Player()
        self.__player2 = Player()
        self.__die = ElectronicDie()
        self.__record = RecordData()

        self.__sense.clear()
        self.__player1.setActive(True)
        self.__player1Points = 0
        self.__player2Points = 0

    def run(self):
        self.startGame()

        while(self.__player1Points < constants.MAX_POINTS and self.__player2Points < constants.MAX_POINTS ):
            #roll a die 
            num = self.__die.checkDie()

            #if the die has been rolled
            if num != 0:
                if self.__player1.getActive():
                    self.__player1.addPoints(num)
                    self.__player1Points += num
                    self.showPointMessage("P1", self.__player1Points)

                    if self.__player1Points >= constants.MAX_POINTS:
                        self.__player1.setWin()
                    else:
                        self.__sense.show_message("Player 2 turn")

                    
                elif self.__player2.getActive():
                    self.__player2.addPoints(num)
                    self.__player2Points += num
                    self.showPointMessage("P2", self.__player2Points)

                    if self.__player2Points >= constants.MAX_POINTS:
                        self.__player2.setWin()
                    else:
                        self.__sense.show_message("Player 1 turn")

                self.__player1.setActive(not self.__player1.getActive())
                self.__player2.setActive(not self.__player2.getActive())

        self.endGame()

    def showPointMessage(self, player, pts):
        self.__sense.show_message("{0} points: {1}\n".format(player, pts))

    def startGame(self):
        intro = """Hello, in this game Player 1 and Player 2 take turns in rolling a die. 
        The first one to roll {0} points is the winner""".format(constants.MAX_POINTS)
        print(intro)
        self.__sense.show_message(intro, scroll_speed=0.07)
        self.__sense.show_message("Player 1 starts",scroll_speed=0.07)

    def endGame(self):
        time = datetime.now().strftime("%H.%M.%S")

        if self.__player1.getWin():
            self.__sense.show_message("Congrats, P1 is the winner with score {0}\n".format(self.__player1Points),scroll_speed=0.07)
            data = {
                'player' : 'Player 1',
                'points' : str(self.__player1.getPoints()),
                'time': time
            }
            self.__record.recordData(data)

        if self.__player2.getWin():
            self.__sense.show_message("Congrats, P2 is the winner with score {0}\n".format(self.__player2Points),scroll_speed=0.07)
            data = {
                'player' : 'Player 2',
                'points' : str(self.__player2.getPoints()),
                'time': time
            }
            self.__record.recordData(data)

