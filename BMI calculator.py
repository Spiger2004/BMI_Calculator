# BMI Calculator

# ⇓⇓First taking data from users⇓⇓
insert1=float(input("Enter your HEIGHT(meter)---->"))
insert2=int(input("Enter your WEIGHT----------->"))
insert3=str("this is your BMI")

# ⇓⇓Putting the formula⇓⇓
bmi=(insert2/(insert1*insert1))

print(bmi, "This is your BMI.")

# ⇓⇓Now giving the conditions⇓⇓
if bmi >24.9:
    print("Yor are over weight try to lose your fat.")
elif bmi <18:
    print("You are under weight try to gain some weight.")
else:
    print("Hurray!, Congratulation your BMI is normal. Maintain this body")


# Created by SPIGER INFINITY