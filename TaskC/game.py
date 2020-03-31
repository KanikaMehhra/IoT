from gameEngine import gameEngine
from player import player
import modules
from electronicDie import electronicDie
from random import randint

#instantiating a die for the game
die=electronicDie()

##instantiating the game engine with the die.
gameEng=gameEngine(die)

#creating players
player1=player("Kanika")
player2=player("Suhani")

#adding players to the engine
gameEng.addPlayer(player1)
gameEng.addPlayer(player2)

#starting the game
gameEng.startGame()