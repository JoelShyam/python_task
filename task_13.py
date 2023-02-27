print("two questions \nthink of an object  and i'll try to guess it.")

q1=str(input("question    1)is it animal,vegetabe or mineral?\n"))

q2=str(input("is it biggerthan a breadbox?\n"))

if q1=="animal":

    if q2=="yes":

        print("i guess that you are thinking of a mouse")

    else:
    
        print("i guess that you are thinking of a squirrel")

elif q1=="vegetable":

    if q2=="yes":

        print("i guess that you are thinking of a watermelon")

    else:

        print("i guess that you are thinking of a carrot")

elif q1=="mineral":

    if q2=="yes":

        print("i guess that you are thinking of a camaro")

    else:

        print("i guessthatyou are thinking of a paper clip")

else:

    print("")

print("i would ask you if i'm right but i don't actually care")