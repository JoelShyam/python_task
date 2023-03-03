tax=0.0825
shipping_cost=5.0
per_keychain_shipping_cost=1.0
cost=10
add=0
reduce=0
def add_keychains():
    while True:
        num=int(input("enter num of keychains to add  "))
        global add
        if num>=0:
            add+=num
            return add
        else:
            print("sorry you have entered a negative num")
def remove_keychains():
    while True:
        remove=int(input("enter num of keychains to be removed  "))
        global reduce
        if remove<=add:
            reduce-=remove
            return reduce
        else:
            print("sorry enter a valid num")
def view_order():
    while True:
        order=add+reduce
        subtotal=cost*order
        shipping=shipping_cost+order
        print("the num of keychains in cart ",order)
        print(f"cost for ordered keychains  ${subtotal}")
        print(f"the shipping cost is ${shipping}")
        print(f"the tax is ${tax}")
        print(f"the total cost is ${subtotal+shipping+tax}")
        break
def checkout():
        name=input("enter your name ")
        view_order()
        print(f"thank you {name} for your order")
while True:
    print("Dhilaharis Shoppeeeeee")
    print("1. Add keychains to order")
    print("2. Remove keychains from order")
    print("3. View current order")
    print("4. Checkout")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        add_keychains()
    elif choice == 2:
        remove_keychains()
    elif choice == 3:
        view_order()
    elif choice == 4:
        checkout()
        break
    else:
        print("Please enter a valid choice.")
