#Python compound interest calculator
principle=0
time=0
rate=0

while True:
    principle=float(input("Enter the principle amount:"))
    if principle< 0:
        print("Principle can't be  less than  0")
    else:
        break


while True:
    rate=float(input("Enter the rate of interest:"))
    if rate<0:
        print("Interest Rate can't be  less than  0")
    else:
        break

while True:
    time=int(input("Enter the time :"))
    if time<0:
        print("Time can't be  less than o 0")
    else:
        break

amount=principle*pow(1+(rate/100),time)
print(f"The final amount after {time} year/s = ${amount:.2f}")