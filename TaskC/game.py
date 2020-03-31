from gameEngine import gameEngine
from player import player
from electronicDie import electronicDie

##instantiating the game engine.
gameEng=gameEngine()

#creating players
player1=player("Kanika")
player2=player("Suhani")
players=[player1,player2]

#adding players to the engine
for player in players:
    gameEng.addPlayer(player)

