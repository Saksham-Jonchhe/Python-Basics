number=input("enter any number:")

def pal():
    palnum=""
    for i in range(len(number),0,-1):
        palnum+=number[i-1]
    return palnum
        

num2=pal()        
print(num2)        

if num2==number:
    print("palindrome")
else:
    print("Not")