sentence = str.lower(input("Enter a sentence: ")).strip()

for word in sentence.split():
    if word[0] in 'aeiou':
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')
