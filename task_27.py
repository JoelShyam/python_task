add = 0
reduce = 0
cost = 0

def add_keychain():
    global reduce
    global add
    add = int(input(f"You have {reduce} keychains. How many to add? "))
    reduce += add
    print(f"Now you have {reduce} keychains.")

def remove_keychain():
    global reduce
    remove = int(input(f"You have {reduce} keychains. How many to remove? "))
    reduce -= remove
    print(f"Now you have {reduce} keychains.")

def current_order():
    global reduce
    global cost
    cost = 10 * reduce
    print(f"Now you have {reduce} keychains.")
    print("Keychains cost $10 each.")
    print(f"Total cost is: ${cost}.")

def checkout():
    global reduce
    global cost
    name = input("What is your name? ")
    print(f"You have {reduce} keychains.")
    print("Keychains cost $10 each.")
    print(f"Total cost is: ${cost}.")
    print(f"Thank you for your order, {name}.")

while True:
    print("Ye Olde Keychain Shoppe")
    print("1. Add keychains to order")
    print("2. Remove keychains from order")
    print("3. View current order")
    print("4. Checkout")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        add_keychain()
    elif choice == 2:
        remove_keychain()
    elif choice == 3:
        current_order()
    elif choice == 4:
        checkout()
        break
    else:
        print("Please enter a valid choice.")
