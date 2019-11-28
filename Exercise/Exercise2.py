# Faulty calculator
# Currectly solve all expression except the following :
# 45 * 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4

operator = input("Enter your operator [+,-,*,/] ")
num1 = int(input("Enter first operand "))
num2 = int(input("Enter second operand "))

if num1 == 56 and num2 == 9 and operator == '+':
    print("Ans : 77")
elif num1 == 45 and num2 == 3 and operator == '*':
    print("Ans : 555")
elif num1 == 56 and num2 == 6 and operator == '/':
    print("Ans : 4")
elif operator == '*':
    print("Ans : ",(num1*num2))
elif operator == '+':
    print("Ans : ",(num1+num2))
elif operator == '-':
    print("Ans : ",(num1-num2))
else :
    print("Ans : ",(num1/num2))


