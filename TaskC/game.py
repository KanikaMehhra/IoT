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
players=[player1, player2]

#adding players to the engine
for player in players:
    gameEng.addPlayer(player)

#starting the game
gameEng.startGame()

#finishing the game
gameEng.gameFinished()