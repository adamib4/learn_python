

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

name = 'Jack'
item = {f'{name}':f'{string_color(name)}'}

print(item)






















'''

import requests

res = requests.get('https://www.color-hex.com/color/7314f1')

page = open('result.html','wb')
for chunk in res.iter_content(100000):
	page.write(chunk)
page.close()


import json
import boto3
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Mycolors')

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
	table.put_item(
   Item={
        'name': 'Adam',
        'color': f'{name}',    
    }
)



    












print('Welcome To "What color is your name!"')

choice = input('Would you like to see what color your name is? y/n: ').lower()

while choice != 'n':
	name = input('Input a name to see what color your name is: ')
	print('Here\'s what your name looks like')
	webbrowser.open(f'https://www.color-hex.com/color/{string_color(name)}')
	choice = input('Would you like to see what color your name is? y/n: ').lower()

print('Exiting. Goodbye!')
'''