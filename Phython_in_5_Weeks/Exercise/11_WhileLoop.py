total = 0

while total < 100:

    text = input('Enter a string: ').strip()


    if text.isdigit():
        total += int(text)
        print(f'Total is {total}')
    else:
        print(f'{text} is not numeric; try again')

print(f'The total is {total}')