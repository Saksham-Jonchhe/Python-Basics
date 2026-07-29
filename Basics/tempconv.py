#Tempearture conversion
unit=input("Enter tempearture unit in (Celsius or Fahrenheit):")
temp=float(input("Enter the temperature:"))

if unit=='C':
    temp=(temp*(9/5))+32
    print(f"The temperature in Fahrenheit:{round(temp,2)}°F")
elif unit=='F':
    temp=(temp-32)*(5/9)
    print(f"The temperature in Celsius:{round(temp,2)}°C")
else:
    print(f"{unit} is unavailable. You have not selected a valid unit")