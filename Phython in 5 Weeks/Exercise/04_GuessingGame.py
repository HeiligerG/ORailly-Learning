# from random import random

secret = 69 # secret = random.randint(1, 100) muss aber alls string ge-parst werden

print(f'The secret is {secret}')
print('I am thinking of a number between 1 and 100.')

guess = input('Take a guess: ')
guess = int(guess)

if guess == secret:
    print('You got it!')
elif guess > secret:
    print('Too high!')
else:
    print('Too low!')