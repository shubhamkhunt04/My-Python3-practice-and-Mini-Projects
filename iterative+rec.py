# Factorial of number

def fact_it(n):
    fact1 = 1
    for i in range(n):
        fact1 = fact1*(i+1)
    return  fact1

def fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact_rec(n-1)
n = int(input("Enter a number "))
print(fact_it(n))
print(fact_rec(n))


# Fibonacci series
def fib_rec(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)

print(fib_rec(n))