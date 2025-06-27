#Print even or odd using functions

def check_evn_odd(num):
    if num % 2 ==0:
        print('Even')
    else:
        print('Odd')

number = int(input('Enter a number: '))
check_evn_odd(number)

