# BMI Calculator

# ⇓⇓First taking data from users⇓⇓
height=float(input("Enter your HEIGHT(meter):"))
weight=int(input("Enter your WEIGHT       :"))


# ⇓⇓Putting the formula⇓⇓
bmi=round((weight/(height*height)),2)

print(f"Your BMI is :{bmi}\nAnd ",end="")

# ⇓⇓Now giving the conditions⇓⇓
if bmi >=24.9:
    print("you are over weight try to lose your fat.")
elif bmi <18:
    print("you are under weight try to gain some weight.")
else:
    print("hurray! Congratulation your BMI is normal. Maintain this body")


# Created by SPIGER INFINITY
# Modified by Rajarshi Mondal