import random
secret_num = random.randint(1,10)

while True:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess == secret_num:
        print('Congratulation! You guessed the Correct')
        break
    elif guess < secret_num:
        print('Your guess is too low, Try again')
    else:
        print('Your guess is too high, Try again')