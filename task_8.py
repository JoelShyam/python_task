name=input("hey, what's your name?     \t")

age=int(input (f"ok, {name} how old are you?\t"))

if(age<16):

    print(f"hey {name}, you can't drive")

    print(f"hey {name}, you can't vote ")

    print(f"hey {name}, you can't rent a car ")

elif(age<18):

    print(f"hey {name}, you can drive ")

    print(f"hey {name}, you can't vote ")

    print(f"hey {name}, you can't rent a car ")

elif(age<25):

    print(f"hey {name}, you can drive")

    print(f"hey {name}, you can vote ")

    print(f"hey {name}, you can't rent a car ")

else:

    print(f"hey {name}, you can do anything that's legal")