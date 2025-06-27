"""
date: 19/06/25
Author: Lucky
Des: Armstrong number
"""

user_value = int(input('Enter a number: '))
orig = user_value
summ=0
while user_value > 0:
    rem = user_value % 10
    summ = summ + (rem ** 3)
    user_value = user_value // 10

if summ == orig:
    print('Armstrong no')
else:
    print('Not Armstrong no')