# IoT

This repo is specifically for PIoT assignment 1 purpose.

There are 3 tasks coded and stored in the repo. All the tasks are coded in python, following the Object Orientated Programming methodology.
The tasks also involve raspberry pi with a sense hat. The tasks are as follows:

Task A- it contains an emoji generator. It takes 3 emoji's 2D arrar and draws them on the raspberry pi at an interval of 3 seconds. It uses
3 different colors to create a single emoji.

Task B- displays temperature every 10 seconds on the dislay after reading values from a file determining which tempreatures                                     are maximum and minimum in appropriate colours. If joystick is pressed it will quit the program (not immediately). Tries to simulate the actual temperature through computing average temperature and subtracking temp of the processor.

Task C- it contains a game designed to be played by 2 players only. There are instruction throughout the game.
        There is an electonicDie.py that detects the movement of the raspberry 
        pi and generates a random number.  The rules or the game are that Player 1 and Player 2 take turns in rolling a die i.e. 
        shaking the pi. The generated random value 
        gets added to the points accumulated by the active player i.i the player who shook the pi. 
        The first one to roll 30 points is the winner. The winner name, points and the time hen game ends are stored in a winner.csv file.
