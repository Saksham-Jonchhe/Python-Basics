
foods= []
prices= []
total=0

while True:
  food=input("Enter a food to buy (q to quit):")
  if food.lower()=="q":
    break
  else:
    price=float(input("Enter the price of the {food}: $"))
    foods.append(food)
    prices.append(price)

print("Your cart has: ")
for food in foods:
  print(food,end=",")

for price in prices:
  total=total+price

print()
print(f"Total= ${total}")
  


 