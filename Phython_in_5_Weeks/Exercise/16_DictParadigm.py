counts = {'vowels':0, 'digits':0, 'others':0}

text = input('Enter a string: ').strip()

for char in text:

    if char in 'aeiou':
        counts['vowels'] +=1
    
    elif char.isdigit():
        counts['digits'] +=1

    else:
        counts['others'] +=1

print(counts)