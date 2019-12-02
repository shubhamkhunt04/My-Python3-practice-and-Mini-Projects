a = 5
b = 10

c = sum((a,b))  # build in function
print(c)


# user define function


def fun1():
    print("hello fun1")

fun1()  # function call


def fun2(x,y):
    """This is a function which will calculate sum of two numbers"""      # this is DOC string
    print("sum is ",x+y)

fun2(14,15)     # function call
print(fun2.__doc__)



def fun3(p,q):
    mul = p*q
    return mul

result = fun3(5,7)
print(result)
