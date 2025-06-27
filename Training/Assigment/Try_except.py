#Question 5
"""num = input("Enter a number: ")
try:
    num1 = int(num)
    print("You entered Number is: ", num1)
except ValueError:
    print("Not a valid integer..!")"""

#Question 6

while True:
    try:
        number = int(input("Enter a valid integer: "))
        print("You entered:", number)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")