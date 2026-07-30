#collection =single "variable" used to store multiple values

#This is a list.ordered and changeable.Duplicates are ok
#fruits=["apple","orange","banana","coconut"]

#This is a set.Unordered and immutabele.No duplicates
#fruits={"apple","orange","banana","coconut"}

#This is a tuple.Ordered and changeable.Duplicates are OK.FASTER
fruits=("apple","orange","banana","coconut")

#print(dir(fruits))
#print(help(fruits))

#print(len(fruits))

#print("apple" in fruits)

#print(fruits[::-1])

#for fruit in fruits:
  #  print(fruit)

#fruits[0]="pineapple"
#fruits.append("pineapple")
#fruits.insert(0,"pineapple")

#fruits.sort()
#fruits.clear()
#print(fruits.count("apple"))
#print(fruits.index("apple"))
#print(fruits)

#fruits.add("pineapple")
#fruits.pop()
#fuits.clear()

print(fruits.index("apple"))
print(fruits.count("coconut"))
print(fruits)