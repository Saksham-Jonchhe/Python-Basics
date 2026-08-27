numbers=int(input("enter a number:"))
arm=numbers
any=len(str(numbers))
cube=0
while numbers!=0:
    temp = numbers%10
    print(temp)
    cube = cube + temp**any
    numbers=numbers//10
    print(numbers)
if cube == arm:
    print("armstrong")
else:
    print("not armstrong")
