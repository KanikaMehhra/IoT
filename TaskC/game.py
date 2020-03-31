from gameEngine import gameEngine
from player import player
import modules
from electronicDie import electronicDie
from random import randint

#set initial orientation of the pi game device.
#initOrientTuple=modules.getCurrentOrientationTuple()

#instantiating a die for the game
#die=electronicDie(randint(1,6),initOrientTuple)
die=electronicDie()

##instantiating the game engine.
gameEng=gameEngine(die)

#creating players
player1=player("Kanika")
player2=player("Suhani")

#adding players to the engine
gameEng.addPlayer(player1)
gameEng.addPlayer(player2)

gameEng.startGame()