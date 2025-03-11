number = input('Give me a number: ').strip()

for index, one_digit in enumerate(number):
    power = len(number) - index -1
    print(f'{one_digit}: * 10**{power}')