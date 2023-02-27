option=input("Are you ready for a quiz?:")
if option=="yes":
    print("ok...,here it comes!")
    print("Q1) What is the capital of Alaska? \n 1)Melbourne    2)Anchorage    3) Juneau")
 
    q1=int(input())
    if q1==1 or q1==2:
        print("Sorry... wrong answer")
    elif q1==3:
        print("That's right answer!")
    else:
        print("oops, you entered an invalid option skipping to next qn")

    print("Q2) Can you store the value ""'cat'""in a variable of type int? \n    1)Yes    2)No")
    q2=int(input())
    if q2==1:
        print("sorry,""cat"" is a string. int can only store numbers")
    elif q2==2:
        print("That's correct")
    else :
        print("qn is skipped due to invalid option")

    print("Q3) What is the result of 9+6/3? \n    1)5    2)11    3) 15/3")

    q3=int(input())
    if q3==1 or q3==3:
        print("Sorry... not a correct answer ")
    elif q3==2:
        print("That's right answer!")
    else:
        print("invalid option !!! ")
    def result():
        if q1==3 and q2==2 and q3==2:
            print("Overall ,you got 3 out of 3......congragulations!!!!")
        elif (q1==3 and q2==2)or(q1==3 and q3==2)or(q3==2 and q2==2):
            print("Overall ,you got 2 out of 3")
        elif q1==3 or q2==2 or q3==2:
            print("Overall ,you got 1 out of 3")
        else:
            print("OOPS!!!sorry you got 0 out of 3")
    result()
else:
    print("ok.. I think You are not ready for this quiz")

