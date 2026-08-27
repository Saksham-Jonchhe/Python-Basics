# Given Input: 76542

# Expected Output: 24567
numbers=0
numbers=int(input("Give a number:"))
reversed_num=0
while numbers !=0:
    reversed_num = (reversed_num*10) + numbers%10
    numbers = numbers//10
    
print(int(reversed_num))