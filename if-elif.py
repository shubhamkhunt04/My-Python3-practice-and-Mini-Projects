num1 = input("Enter num1 ")
num2 = input("Enter num2 ")

if num1 < num2 :
    print("num2 is greater")
elif num1 == num2:
    print("both are equal")
else:
    print("num1 is greater")


list = [ 1, 2, 3, 4, 5, 6]

print(3 in list)       # true
if 3 in list:
    print("Yes 3 is present in the list")

print(10 not in list)  # true
if 10 not in list:
    print("10 is not present in the list")