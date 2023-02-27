h=float(input("your height in metres   \t"))
w=float(input("your weight in kilograms\t"))
bmi=float(w/(h**2))
print(f"\nyour BMI is {bmi}")
if bmi<18.5:
    print("bmi category: underweight")
elif (bmi>=18.5)and(bmi<=24.9):
    print("bmi category: normalweight")
elif (bmi>=25.0)and(bmi<=29.9):
    print("bmi category: overweight")
elif(bmi>=30.0):
    print("bmi category: obese")