import sys
import random

def RPS(user):
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

def toss():
    outcomes = ['Heads', 'Tails']
    return random.choice(outcomes)

'''
change this to another controller
'''
def getAnswer(q, alfred):
    if 'toss' in q.lower():
        return toss()
