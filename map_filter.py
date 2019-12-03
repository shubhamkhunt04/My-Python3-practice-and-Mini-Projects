# use of map function
number = ["1","2","3","4"]

print(number)
for i in range(len(number)):
    number[i] = int(number[i])
print(number)


# Easy way
#1
number = list(map(int,number))   # map(functinname,passlist)
print(number)

#2
squre = list(map(lambda x:x*x,number))
print(squre)

#3
def squre(a):
    return  a*a
def cube(a):
    return  a*a*a

func = [squre,cube]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)


# use of filter function

list1 = [1,2,3,4,5,6,7,8,9]

def greter5(num):
    return num>5

result = list(filter(greter5,list1))
print(result)

# use of reduce function
from  functools import reduce
list = [1,2,3,4,5]
num = reduce(lambda x,y : x+y,list)
print(num)