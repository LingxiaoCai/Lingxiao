

def add(num1, num2):
    return num1 + num2
  
def min(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def calculator():
    print('select type of operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    selection = int(input('enter your selection:'))
    num1 = float(input('enter your number 1:'))
    num2 = float(input('enter your number 2:'))
    if selection == 1:
        print(add(num1, num2))
    elif selection == 2:
        print(min(num1, num2))
    elif selection == 3:
        print(mul(num1, num2))
    elif selection == 4:
        print(div(num1, num2))
    else:
        print('Error')

calculator()


    
