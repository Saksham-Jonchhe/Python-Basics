""""
name=input("Enter your name:")
while name=="":
    print("you did not end anything")
    name=input("Enter your name:")

print(f"Hello {name}")
"""

food=input("Enter the food you like: (q to quit)")

while not food=='q':
    print(f"You like {food}")
    food=input("Enter the food you like: (q to quit)")
