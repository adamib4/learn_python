
def add(x , y):
    """Add two number"""
    return x + y

def subtract(x,y):
    """Substract two number"""
    return x - y

def multiply(x,y):
    """Multiply two number"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    return x / y

def modulus(x, y):
    """Return the remainder (modulus) of two numbers"""
    return x % y

def power(x, y):
    """Raise number to the power of given number"""
    return x ** y

def check_if_user_has_finished():
    """
    checks that the user wants to finish or not.
    Perform some verification of the input.
    """
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input("Do you want to finish (y/n): ").lower()
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
        return ok_to_finish

def get_ops_choice():
    input_ok = False
    while not input_ok:
        print("Menu options are: ")
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3 Mulitply')
        print('\t4 Divide')
        print('\t5 Modulus')
        print('\t6 Power')
        print('--------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1','2','3','4','5','6'):
            input_ok = True
        else:
            print('Invalid input (must be 1-6)')

    return user_selection

def get_number_from_user():
    num1 = get_integer_input('Input first number: ')
    num2 = get_integer_input('Input Second number: ')
    return num1, num2

def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('Input must be an integer')
        value_as_string = input(message)
    return float(value_as_string)


finished = False

while not finished:
    result = 0
    menu_choice = get_ops_choice()
    number1, number2 = get_number_from_user()
    if menu_choice == '1':
        result = add(number1, number2)
    elif menu_choice == '2':
        result = subtract(number1, number2)
    elif menu_choice == '3':
        result = multiply(number1, number2)
    elif menu_choice =='4':
        result = divide(number1, number2)
    elif menu_choice == '5':
        result = modulus(number1, number2)
    else:
        result = power(number1, number2)
    print(f'Result: {result}')
    print('=============================')
    finished = check_if_user_has_finished()


print("Bye")