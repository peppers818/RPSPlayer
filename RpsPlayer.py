#Samantha Holloway 11/2014
#Rock Paper Scissors implementation of Player class
#A gambit is a predetermined RPS strategy
#AI uses 1 of 8 famous gambits randomly for a match
#Edited by Joseph Pannizzo
import random

class RpsPlayer():
    def __init__(self):
        self.move = random.randint(1,8)# choose random gambit
        self.currentMove = 0
        
    #Provides AI for making a move, returns move as a string
    #move is either Rock(0), Paper(1), or Scissors(2)
    def play(self):
        if self.move == 1: #Denoument gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "0"
            elif self.currentMove == 2:
                return "2"
            else:
                return "1"   
        elif self.move == 2: #Bureaucrat gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "1"
            elif self.currentMove == 2:
                return "1"
            else:
                return "1" 
        elif self.move == 3: #Crescendo gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "1"
            elif self.currentMove == 2:
                return "2"
            else:
                return "0" 
        elif self.move == 4: #Avalanche gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "0"
            elif self.currentMove == 2:
                return "0"
            else:
                return "0" 
        elif self.move == 5: #Fistfull o' Dollars gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "0"
            elif self.currentMove == 2:
                return "1"
            else:
                return "1" 
        elif self.move == 6: #Paper Dolls gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "1"
            elif self.currentMove == 2:
                return "2"
            else:
                return "2" 
        elif self.move == 7: #Scissor Sandwich gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "1"
            elif self.currentMove == 2:
                return "2"
            else:
                return "1" 
        else: #move == 8, Toolbox gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "2"
            elif self.currentMove == 2:
                return "2"
            else:
                return "2" 

r = RpsPlayer()
print(r.play())
print(r.play())
print(r.play())