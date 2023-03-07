print("**********BMI Calculator**********")

name=input("Enter Your Name")
age=input("Enter Your AGE")
weight=int(input("Enter your Weight in Pounds"))
height=int(input("Enter your Height in Inches"))
bmi=(weight*703)/ (height*height)
print(name,"Your BMI is:",bmi)


if bmi>0:
    if bmi<=18.4:
        print(name,"You are UNDERWEIGHT")
    elif bmi<24.9:
        print(name,"You are NORMAL")
    elif bmi<39.9:
        print(name,"You are OVERWEIGHT")
    else:
        bmi>=40
        print(name,"You are OBESE")
else:
    print("Enter a Valid Value")



print("----------Have a Great Day------------")