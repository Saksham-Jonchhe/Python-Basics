# Given Input: 75869
#Use while loop
# Expected Output: Total digits are: 5

numbers=int(input("Enter a number:"))
count=0
while numbers!=0:
        numbers=numbers//10
        count+=1
print(f"Total digits are:{count}")    