list1 = [10, 20, 30, 40, 50]
#Expected Output: [50, 40, 30, 20, 10]

print("[",end="")
for i in range(len(list1),0,-1):
    pr=print(list1[i-1],end=" ")
   
print("]")