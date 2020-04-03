import sys
def getInventory():
    inventory = {}
    print('Inventory: ')
    while True:
        name = input()
        if name == '':
            break
        if name in inventory:
            answer = input('Would you like the update the inventory? Y/N')
            if answer == 'Y':
                amount == int(input('How many?'))
                inventory[name] = amount
                
        else:
            amount = int(input('amount: '))
            inventory.setdefault(name,amount)
    return inventory

spam = getInventory()
addition = 0

for v in spam.values():
    addition += v
print(f'Total number of Items: {addition}')
    
            

            
            
        


                              
                              
