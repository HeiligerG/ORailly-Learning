name = input('Whats your name: ').strip()

# nameLen = len(name)
index = 0

for i in range(len(name)):
    # index += 1
    print(name[:i+1]) # index = i