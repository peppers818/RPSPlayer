#Samantha Holloway, Joseph Pannizzo 11/2014
#Rock Paper Scissors implementation of Player class
#A gambit is a predetermined RPS strategy
#AI uses 1 of 8 famous gambits randomly for a match

import random

class RpsPlayer():
    def __init__(self):
        self.move = random.randint(1,8)  # choose random gambit
        self.currentMove = 0
        
    #Provides AI for making a move, returns move as a string
    #move is either Rock, Paper, or Scissors
    def play(self):
        if self.move == 1: #Denoument gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Rock"
            elif self.currentMove == 2:
                return "Scissors"
            else:
                return "Paper"   
        elif self.move == 2: #Bureaucrat gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Paper"
            elif self.currentMove == 2:
                return "Paper"
            else:
                return "Paper" 
        elif self.move == 3: #Crescendo gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Paper"
            elif self.currentMove == 2:
                return "Scissors"
            else:
                return "Rock" 
        elif self.move == 4: #Avalanche gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Rock"
            elif self.currentMove == 2:
                return "Rock"
            else:
                return "Rock" 
        elif self.move == 5: #Fistfull o' Dollars gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Rock"
            elif self.currentMove == 2:
                return "Paper"
            else:
                return "Paper" 
        elif self.move == 6: #Paper Dolls gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Paper"
            elif self.currentMove == 2:
                return "Scissors"
            else:
                return "Scissors" 
        elif self.move == 7: #Scissor Sandwich gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Paper"
            elif self.currentMove == 2:
                return "Scissors"
            else:
                return "Paper" 
        else: #move == 8, Toolbox gambit
            self.currentMove += 1
            if self.currentMove == 1:
                return "Scissors"
            elif self.currentMove == 2:
                return "Scissors"
            else:
                return "Scissors"