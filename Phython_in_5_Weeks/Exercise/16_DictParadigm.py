counts = {'vowels':[], 'digits':[], 'others':[]}

text = input('Enter a string: ').strip().lower()

for char in text:

    if char in 'aeiou':
        counts['vowels'].append(char)

    elif char.isdigit():
        counts['digits'].append(char)

    else:
        counts['others'].append(char)

print(counts)