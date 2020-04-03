'''
This program will flip coin 100 times and store the result in a list called spam.
I'm also going to look at how often a Six streak occurs.

'''
import random

def generateHT():
    spam= []
    for item in range(10000):
        spam.append(random.choice('HT'))
##    print(spam)
    return spam

def streaks(spam):
    HeadCounter = 0
    TailCounter = 0
    for i in range(len(spam)):
        if spam[i] == 'H' and spam[i-1] == 'H'and spam[i-2] == 'H'and spam[i-3] == 'H' and spam[i-4] == 'H'and spam[i-5] == 'H':
            HeadCounter +=1
        if spam[i] == 'T' and spam[i-1] == 'T' and spam[i-2] == 'T'and spam[i-3] == 'T' and spam[i-4] == 'T'and spam[i-5] == 'T':
            TailCounter +=1
    print(f'TAils Streak: {TailCounter} and Heads Streak: {HeadCounter}')



streaks(generateHT())
