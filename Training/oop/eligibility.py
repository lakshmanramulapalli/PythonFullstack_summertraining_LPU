"""
from myexceptions.prjexceptions import AgeLimitError

per_name = input('Name: ')
per_age = int(input('Age: '))

try:
    if per_age < 18:
        raise AgeLimitError('Not Eligible')
except AgeLimitError as ale:
    print(ale)
else:
    print('You are Eligible')
"""

x=1
y=1
z=1
n=2

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                print([i,j,k])
#print([ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k !=n)])
