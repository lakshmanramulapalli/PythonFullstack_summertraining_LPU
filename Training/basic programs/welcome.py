print('Hello World !!!')

num1=10
num2=20

print(f'Sum: {num1 + num2}')
print(f'Diff: {num1 - num2}')
print(f'Pro: {num1 * num2}')
print(f'Quo: {num1 // num2}')

#res = (num1 > num2) ? 'Num1 is big': 'Num1 is big'.... {Error}
res = 'Num1 is big' if (num1>num2) else 'Num2 is big'
print(res)
