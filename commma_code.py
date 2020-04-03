import sys
'''
Chapter 4 of automate the boring stuff projects.
This funtion will take a list value as an argument and returns a string
with all the items separated by a comma and a space,
with and inserted before the last item.'''

def comma_code(list_of):
    if len(list_of) == 0:
        print('This an empty list')
        sys.exit()
    list_of[-1]= ''.join('and ' + list_of[-1])
    print(list_of)  
    



