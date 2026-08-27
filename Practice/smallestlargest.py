numbers=int(input("Enter a number:"))
largest=0
smallest = numbers%10
while(numbers!=0):
    temp = numbers%10
    if temp >= largest:
        largest = temp
    elif temp <= smallest:
        smallest = temp
    numbers=numbers//10
print(largest,smallest)



