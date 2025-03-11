total = 0

menu = { 'sandwich':10, 'tea': 8 , 'apple':3, 'cake':10}

while True:
    order = input('What do you want to order? ').strip().lower()

    if order == '':
        break

    if order in menu:
        price = menu[order]
        total += price
        print(f'The {order} is {menu[order]}, your total is now {total}')

    else:
        print(f'Sorry we are out of {order} today.')

print(f'total is {total}')