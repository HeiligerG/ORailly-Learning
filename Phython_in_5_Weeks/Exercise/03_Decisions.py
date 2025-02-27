#Exercise 1: What comes first in the Alphabet
first = input("Enter first word: ")
second = input("Enter second word: ")

if first < second:
    print(f'{first} comes before {second}.')
else:
    print(f'{second} comes before {first}.')

#Exercise 2: Is it the same or what comes first in the Alphabet
if first == second:
    print(f'{first} is the same as {second}!')
elif first < second:
    print(f'{first} comes before {second}.')
else:
    print(f'{second} comes before {first}.')


#Exercise 3:
my_name = 'Holy'
my_company = 'WishFoundation'

name = input("Enter your name: ")
company = input("Enter your company: ")

if name == my_name and company == my_company:
    print(f'If your name is {my_name} and your company\'s name is {my_company}. You must be me!')
elif name == my_name:
    print(f'If your name is {name}, you have a cool name!')
elif company == my_company:
    print(f'If your company\'s name is {company}, hello my dear colleague!')
else:
    print(f'WOW, your name is {name} and your company\'s name is {company}, interesting!')
