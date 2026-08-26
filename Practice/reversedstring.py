#Given Input: "Python"
# Original: Python
# Reversed: nohtyP


name=input("Enter a string:")
reversed_str=""
for i in range(len(name),0,-1):
    reversed_str=name[i-1]
    print(reversed_str,end="")
