num1=int(input())
num2=int(input())
nums = [1,2,3]
ans=0

try:
    ans = num1//num2
    elmt = nums[2]
except ZeroDivisionError:
    print("Don't give 0 in num2")

except IndexError:
    print('Watch the index')

#We can only use single except for any error excemption
except:
    print('Oops something went wrong')
else:
    print(f'Quo: {ans}')
    print(f'Element: {elmt} ')

finally:
    print('Done')


