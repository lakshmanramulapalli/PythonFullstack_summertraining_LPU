"""
19/06/25
Lucky
simple menu driven calculator
"""

num1 = int(input('Enter first num: '))
num2 = int(input('Enter second num: '))
user_choice = float(input('1.Add 2.Sub 3.Mul'))

'''
if user_choice == 1:
    print(f'Sum: {num1+num2}')
elif user_choice == 2:
    print(f'Sub: {num1-num2}')
elif user_choice == 3:
    print(f'Prod: {num1*num2}')
'''

match user_choice:
    case 1.0: #Python allows floating point values
        print(f'Sum: {num1+num2}')
    case 2:
        print(f'Sub: {num1-num2}')
    case 3:
        print(f'prod: {num1* num2}')

    case _:
        print('Enter between 1-3')

print('Done..!!')