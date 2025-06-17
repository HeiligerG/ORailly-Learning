rainfall = {}

while True:
    name = input('Enter a City name: ').strip()

    if name == '':
        break

    mm_rain = input(f'How much rain (in mm) fell in {name}?')
    mm_rain = int(mm_rain)
    
    if name in rainfall:
        rainfall[name] += mm_rain
    else: 
        rainfall[name] = mm_rain

for key, value in rainfall.items():
    print(f'{key}: {value}')

