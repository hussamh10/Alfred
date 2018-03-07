import sys
import random
from modules.module import Module

class Games(Module):
    def __init__(self):
        super(Games, self).__init__("Games")

    def RPS(self, user):
        bot = random.randint(0, 2)
        choices = ['Rock', 'Paper', 'Scissors']

        outcome = 'Tied'

        if(user == 0):
            if(bot == 1):
                outcome = 'Lost'
            if(bot == 2):
                outcome = 'Won'

        if(user == 1):
            if(bot == 2):
                outcome = 'Lost'
            if(bot == 0):
                outcome = 'Won'

        if(user == 2):
            if(bot == 0):
                outcome = 'Lost'
            if(bot == 1):
                outcome = 'Won'

        return 'Alfred chose ' + choices[bot] + '\n' + 'You chose ' + choices[user] + '\n' + 'You ' + outcome

    def toss(self):
        outcomes = ['Heads', 'Tails']
        return random.choice(outcomes)

    def getAnswer(self, query, alfred):
        query = query.lower().split()

        if 'toss' in query:
            return self.toss()

        if 'rps' in query:
            return self.RPS(query.split()[1])
