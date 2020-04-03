from string import ascii_lowercase
from itertools import count
def alphabet_position(text):
    alphabet = dict(zip(ascii_lowercase,count(1)))
    result = ''
    for letter in text.lower():
    	if letter.isalpha():
	    	result += str(alphabet[letter])+ ' '
    return result

    

print(alphabet_position("The sunset sets at twelve o' clock."))
print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")





# # alphabet_position('adam ibrahim')
# name = "The narwhal bacons at midnight."
# result = ''
# alphabet = dict(zip(ascii_lowercase,count(1)))
# for letters in name.lower():
# 	if letters.isalpha():
# 		result += str(alphabet[letters])+ ' '

# print(result)