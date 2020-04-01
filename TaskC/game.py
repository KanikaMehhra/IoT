from gameEngine import GameEngine
from player import Player
from electronicDie import ElectronicDie
from random import randint

#instantiating a die for the game
die=ElectronicDie()

##instantiating the game engine with the die.
gameEng=GameEngine(die)

#creating players
player1=Player("Kanika")
player2=Player("Suhani")

#adding players to the engine
gameEng.addPlayer(player1)
gameEng.addPlayer(player2)

#starting the game
gameEng.startGame()

#finishing the game
gameEng.gameFinished()