# Do names have colors?

# Now they do.

# Make a function that takes in a name (Any string two chars or longer really, but the name is the idea) and use the ascii values of it's substrings to produce the hex value of its color! Here is how it's going to work:

#     The first two hexadecimal digits are the SUM of the value of characters (modulo 256).
#     The second two are the PRODUCT of all the characters (again, modulo 256, which is one more than FF in hexadecimal).
#     The last two are the ABSOLUTE VALUE of the DIFFERENCE between the first letter, and the sum of every other letter. (I think you get the idea with the modulo thing).

# For example "Jack" returns "79CAE5", which is... baby blue!

# "Jack"  #  "J" = 74, "a" = 97, "c" = 99, "k" = 107

# 74 + 97 + 99 + 107 = 377                   -->  mod 256 = 121  -->  hex: 79
# 74 * 97 * 99 * 107 = 76036554              -->  mod 256 = 202  -->  hex: CA
# 74 - (97 + 99 + 107) = -229  --> abs: 229  -->  mod 256 = 229  -->  hex: E5

# NOTE: The function should return None/nil when the input is less than two chars.
# I'll be using webbrowser library to open color-hex.com to view color in webbrowser.

import webbrowser

def hex_format(value):
	result = ''
	for num in value.values():
		result += format((num % 256),'02X')
	return result

def string_color(name):
	result= {'sums':0,'product':1,'abs':0}
	if len(name) >1 :		
		for i in name:
			result['sums'] += ord(i)
			result['product'] *= ord(i)
		for char in range(1,len(name)):
			result['abs'] += ord(name[char])
		result['abs'] = abs(ord(name[0]) - result['abs'])
		return hex_format(result)
	else:
		print('Lengths too short. Name must be at least two characters long.' )
		return None

print('Welcome To "What color is your name!"')

choice = input('Would you like to see what color your name is? y/n: ').lower()

while choice != 'n':
	name = input('Input a name to see what color your name is: ').lower()
	print('Here\'s what your name looks like')
	try:
		webbrowser.open(f'https://www.color-hex.com/color/{string_color(name)}')
	except:
		webbrowser.open('https://www.google.com/')
	choice = input('Would you like to see what color your name is? y/n: ').lower()

print('Exiting.\nGoodbye!')




