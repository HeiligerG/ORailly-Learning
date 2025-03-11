total = 0

digits = input('Enter a string with digits ').strip()

for string in digits:
    if string == '.':
        break

    if not string.isdigit():
        print(f'{string} is not a digit; ignoring')
        continue

    total += int(string)

print(f'the total is {total}')