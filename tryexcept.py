
try:
    number1 = int(input("Enter first number "))
    number2 = int(input("Enter second number "))
    print("The sum of these two number is ",number1+number2)

except Exception as e:
    print(e)

print("always run")
