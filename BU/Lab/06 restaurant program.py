MENU = {
    'F01': ('Pan Fried Egg', 125.00),
    'F02': ('Grilled Sandwich', 145.00),
    'F03': ('Spaghetti Olio', 169.00),
    'F04': ('Caesar Salad', 139.00),
    'D01': ('Coffee', 120.00),
    'D02': ('Soft Drink', 90.00)
}

IN_CART = {
    'F01': 0,
    'F02': 5,
    'F03': 0,
    'F04': 0,
    'D01': 4,
    'D02': 0
}

def main():
    # I'm not formatting this again -Euryn
    print('''\
.................................................
                  BU Restaurant
                  Menu
.................................................
Menu ID Menu Price
 F01 Pan Fried Egg 125
 F02 Grilled Sandwich 145
 F03 Spaghetti Olio 169
 F04 Caesar Salad 139
 D01 Coffee 120
 D02 Soft Drink 90
.................................................''')
    stop = False
    while not stop:
        stop = True
        menu_id = input('Enter Menu ID: ')

        # If the code is not in menu skip everything and re-ask
        if menu_id not in MENU.keys():
            print('Invalid Code! Please try again.')
            continue
        
        quantity = int(input('Enter quantity: '))
        IN_CART[menu_id] += quantity

        q = input('Quit(Y/N): ')
        if q == 'Y':
           stop = True
    else:
        discount_modifier = 0.0 if input('BU Member Card (Y/N):') != 'Y' else -0.1
        food_total = 0
        drink_total = 0
        print('''\
.................................................
 BU Restaurant
 Receipt
.................................................
 Menu QTY Price''')

        for in_cart, menu in zip(IN_CART.items(), MENU.values()):
            key, quantity = in_cart
            name, price = menu
            if quantity == 0:
                continue
            if key.startswith('F'):
                food_total = food_total + (quantity * price)    
            else:
                drink_total = drink_total + (quantity * price)
            print(name, quantity, quantity*price)
        print('.................................................')
        
        total = food_total + drink_total
        discount = food_total * discount_modifier
        tax = total * 0.07
        net = total + discount + tax
        
        print(f'''\
        Price: {total:.2f}
        discount (only food): {discount:.2f}
        tax: {tax:.2f}
        net: {net:.2f}''')


if __name__ == '__main__':
    main()
