#Python weight converter
import math
weight=float(input("Enter your weight:"))
unit=input("Kilograms or pOunds?(K or L):")

if unit=="K":
    weight=weight * 2.205
    unit="lbs."
    print(f"Your weight is :{round(weight,1)} {unit}")
elif unit=="L":
    weight=weight/2.205
    unit="Kgs."
    print(f"Your weight is :{round(weight,1)} {unit}")
else:
    print(f"{unit} is not valid")



