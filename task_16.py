gender=input("what is  your gender?    ")
fname=input("first name : ")
lname=input("last name  : ")
age=int(input("age  : "))
if gender=='m' and age>=20:
    print(f"then i shall call you Mr.{fname} {lname}")
elif gender=='f'and age>=20:
    marriage=input(f"are you married, {fname} ?(yes/no)")
    if marriage=='yes':
        print(f"then i shall call you Mrs. {fname} {lname}")
    elif marriage=='no':
        print(f"then i shall call you Ms. {fname} {lname}")
elif (gender=='m'or gender=='f')and age<20:
    print(f"then i shall call you {fname} {lname}")