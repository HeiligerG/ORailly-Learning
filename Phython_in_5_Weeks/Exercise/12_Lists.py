vowels = []
digits = []
others = []

input_string = str.lower(input("Enter a string: ").strip())

for item in input_string:
    if item in 'aeiou':
        vowels.append(item)
    elif item.isdigit():
        digits.append(item)
    else:
        others.append(item)
        
print(vowels)
print(digits)
print(others)