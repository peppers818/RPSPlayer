#Samantha Holloway, Joseph Pannizzo 11/2014
#Help/code pieces from Dr. Ganesh Baliga
#Rock Paper Scissors implementation of Player class
#A gambit is a predetermined RPS strategy
#AI uses 1 of 8 famous gambits randomly for a match

import Player
import Message
import random

class SHJPPlayer():
    def __init__(self):
        #Call super class constructor
        Player.Player.__init__(self)
        self.history = ""
        self.reset()

    def play(self):
        return SHJPPlayerStrategy.play

    def reset(self):
        self.history = ""

    def notify(self,message):
        self.history = message  #We don't use history for our strategy

    def get_name(self):
        return "Sam-n-Joe"

class SHJPPlayerStrategy(object):

    def __init__(self):
        self.move = random.randint(1,8)  # choose random gambit
        self.currentMove = 0

    #Provides AI for making a move, returns move as a string
    #move is either Rock(0), Paper(1), or Scissors(2)
    @staticmethod
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

if __name__ == "__main__":
    player = SHJPPlayer()
    opponent = SHJPPlayer()
    players = [opponent,player]
    fakeinfo = ((0,1),1)
    fakeresult = 1
    fakemoves = (1,2)
    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print ("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players,fakemoves,fakeresult))
