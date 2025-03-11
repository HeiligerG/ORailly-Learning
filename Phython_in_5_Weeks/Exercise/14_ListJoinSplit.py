short = []
long = []

sentence = input('Enter a sentence: ').strip()

for word in sentence.split():
    if len(word) < 4: 
        short.append(word)
    else:
        long.append(word)
        
print(' '.join(short))
print(' '.join(long))