x = 8         # global variable
def fun():
    x = 10    # local variable
    print(x)


fun()         # 10
print(x)      # 8
