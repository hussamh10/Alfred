import random
import pprint
import praw
import sys


authentication = open('authentication.local', 'r').readlines()
praw.reddit.read_only = True
bot = praw.Reddit(user_agent='Alfred v0.1',
                  client_id='OoYLyu-_HnuIIA',
                  client_secret='m2ZY_l0LBEF3h6TInLOt1tCkHaw',
                  username=authentication[0][:-1],
                  password=authentication[1][:-1])

def getSubreddit(r):
    submissions = []
    for submission in bot.subreddit(r).hot(limit=7):
        submissions.append(submission.title + '\n' + '-' + '\n' + submission.selftext + '\n' + '-' + '\n' + submission.url)
    return submissions
