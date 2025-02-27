# Input converted to all lower with a Method --> Functions would be len(), print(), input() usw.
text = input(str.lower("Enter one word: "))

vowels = ['a', 'e', 'i', 'o', 'u']

if text[0] in vowels: # Or 'aeiou' da wir strings als collections oder container sehen
    print(f'{text}way')
else:
    textFromOne = text[1:]
    firstChar = text[0]
    print(f'{textFromOne}{firstChar}ay')