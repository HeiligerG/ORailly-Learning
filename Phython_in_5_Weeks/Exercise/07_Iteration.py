vowels = 0
digits = 0
others = 0

input_string = str.lower(input("Enter a string: ").strip())

for i in input_string:
    if i in 'aeiou':
        vowels += 1
    elif i in '0123456789': # .isdigit()
        digits += 1
    else:
        others += 1

print(f"You have {vowels} vowels in your string")
print(f"You have {digits} digits in your string")
print(f"You have {others} others in your string")

# Best to see what is really going on: https://pythontutor.com/