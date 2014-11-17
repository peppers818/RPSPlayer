#Samantha Holloway 11/2014
#Rock Paper Scissors implementation of Player class
import random

class RpsPlayer():
    def __init__(self):
        self.turnOne = True
    #Provides AI for making a move, returns move as a string
    #move is either Rock, Paper, or Scissors
    def play(self):
        if(self.turnOne is False): #Not the first turn
            move = 1 #algorithm should go here to make move
                                #Plan to have list of previous moves
        else: #Turn one, make a random move
            move = random.randint(1,3)
            self.turnOne = False #First turn is done
        if move == 1:
            return "Rock"
        elif move == 2:
            return "Paper"
        else: #move == 3
            return "Scissors"


r = RpsPlayer()
print(r.play())
print(r.play())