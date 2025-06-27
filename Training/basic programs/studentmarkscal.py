"""
date: 19/06/25
Author: Lucky
Des: Student marks calculation
"""

def calc_tot_avg(mark1, mark2, mark3):
    tot = mark1 + mark2 + mark3
    avg = tot / 3
    return tot, avg

sname = input('Enter Student name: ')
mark1 = int(input('Enter marks 1: '))
mark2 = int(input('Enter marks 2: '))
mark3 = int(input('Enter marks 3: '))

total, average = calc_tot_avg(mark1, mark2, mark3)
print(f'Name : {sname} Total: {total} Average: {average}')

