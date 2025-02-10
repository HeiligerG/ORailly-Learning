text = input("Enter a sentence: ")

index = int(input("Enter a number: "))

if index < 0:
    print("The number cannot be negative")
elif index >= len(text):
    print("The number cannot be greater than the length of the sentence")
else:
    char = text[index]
    print(f'The character "{char}" is the {index}. in the sentence')