import sys

'''
The following code creates a collatz function.
Given any number, The function will print a sequence until returns 1'''

def collatz(number):
    if number == 1 or number == 0:
        print(number)
        sys.exit()
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    number = int(input('Enter a number: '))
    while number != 1:
                 number = collatz(number)
except:
                 print('Input a number that\'s larger than 1')
