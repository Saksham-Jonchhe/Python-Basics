squared = lambda num: num*num

print(squared(2))

addTwo=lambda num : num + 2
print(addTwo(12))

sum_total=lambda a, b : a + b
print(sum_total(12,8))

######################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print (addTen(7))
print (addTwenty(7))

#######################

numbers = [3,7,12,18,20,21]

squared_nums= map(lambda num : num * num, numbers)
print(list(squared_nums))

###############


odd_nums = filter(lambda num:num % 2 != 0, numbers)
print(list(odd_nums))


######################

from functools import reduce

numbers = [1,2,3,4,5,1]
total=reduce(lambda acc, curr: acc + curr ,numbers,10)

print(total)

print(sum(numbers,10))




names =['Dave Grey','Sara ITo','John jacob JIngleSchimdt']

char_count= reduce(lambda acc, curr: acc + len(curr), names , 0)

print(char_count)
####################


numbers=[1,2,26,4,18]
max_val=reduce(lambda a,b : a if a>b else b,numbers)
print(max_val)

################

min_val=reduce(lambda a,b: a if b>a else b ,numbers)
print (min_val)

###############

newnumber=[2,1,4,5,6]
square=map(lambda num:num*num,newnumber)
print(list(square))

#############
 
even_nums1=filter(lambda num: num%2==0,newnumber)
print(list(even_nums1))


