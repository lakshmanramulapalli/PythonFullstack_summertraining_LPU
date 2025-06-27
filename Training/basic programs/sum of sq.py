"""
date: 19/06/25
Author: Lucky
Des: Sum of the squares
"""
num = int(input('Enter number of terms: '))
summ=0
for n in range(1,num+1):
#for n in range(1, num+1,2):

    summ += n**2
print(f'Sum of squares {summ}')