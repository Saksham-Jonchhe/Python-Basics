numbers=int(input("enter a number:"))
arm=numbers
anydigit=len(str(numbers))
cube=0
while numbers!=0:
    temp = numbers%10
    cube = cube + temp**anydigit
    numbers=numbers//10
    
if cube == arm:
    print("armstrong")
else:
    print("not armstrong")
