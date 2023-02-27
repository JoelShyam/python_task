weight=float(input("please enter your current earth weight "))

print("i have information for the following planets")

print("    1.venus     2.mars      3.jupiter\n    4.saturn    5.uranus    6.neptune")

visit=str(input("which planet are you vsiting?  "))

if visit=='venus':

    print(f"your weight would be {weight*0.78} pounds on venus")

elif visit=='mars':

    print(f"your weight would be {weight*0.39} pounds on mars")

elif visit=='jupiter':

    print(f"your weight would be {weight*2.65} pounds on jupiter")

elif visit=='saturn':

    print(f"your weight would be {weight*1.17} pounds on saturn")

elif visit=='uranus':

    print(f"your weight would be {weight*1.05} pounds on uranus")

elif visit=='neptune':

    print(f"your weight would be {weight*1.23} pounds on neptune")

else:

    print("enter a valid option")