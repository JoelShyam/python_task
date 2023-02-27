print("welcome to joel's adventures:\n")
opt1=input("you're in a creepy house! wouldyou like to upstairs or kitchen?")
if opt1=="kitchen":
    a=input("there is a long countership with dirty dishes everywhere. off to one side there is as you'd expect, a refrigerator. you may  open the refrigerator orlook into cabinet.")
    if a=="refrigerator":
        a1=input("inside the refrigerator you see food andstuff. it looks pretty tasty. would youlike to eat? (yes or no)")
        if a1=="yes":
            print("you can survive for sometime")
        elif a1=="no":
            print("you die of starvation...eventually")
    elif a=="cabinet":
        a2=input("get the spices or leave? ")
        if a2=="get":
            print("I got the spices")
        elif a2=="leave":
            print("I dont need ")
elif opt1=="upstairs":
    b=input("going through upstairs you'll see a room at right and balcony  at left. (room or balcony) ")
    if b=="room":
        print("take rest")
    elif b=="balcony":
        print("jump and die..")