name=input("hey, what's your name?     \t")

age=int(input (f"ok, {name} how old are you?\t"))

if(age<16):

    print(f"hey {name}, you can't drive or vote or rent a car")

elif((age>=16)and(age<18)):

    print(f"hey {name}, you can drive but you can't vote or rent a car")

elif((age>=18)and(age<25)):

    print(f"hey {name}, you can drive and vote but you can't rent  a car")

else:

    print(f"hey {name}, you can do anything that's legal")