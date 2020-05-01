
'''
In this kata, you must create a digital root function.A digital root is the recursive sum of all the digits in a
 number.Given n, take the sum of the digits of n.If that value has more than one digit, continue reducing in this way
 until a single-digit number is produced.This is only applicable to the natural numbers.

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
'''



def digital_root(n):
   n = list(map(int,str(n)))
   result = sum(n)
   while len(list(map(int,str(result)))) > 1:
   	result = digital_root(result)
   return result




