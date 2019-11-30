# Pattern Printing

# Take one integer ( for n number of rows )
# Take one boolean variable
    # if boolean variable is true then print
    #     *
    #     **
    #     ***
    #     ****
    # if boolean variable is false then print
    #     ****
    #     ***
    #     **
    #     *

n = int(input("Enter a number "))

boolvar = int(input("Enter 1 or 0  "))

b = bool(boolvar)

if(b):
    print("boolean variable b is true")
    for a in range(1,n+2):
        for b in range(1,a):
            print("*", end="")
        print(" ")

else:
    print("boolean variable b is false")
    for i in range(1,n+2):
        for j in range(1,n+2-i):
            print("*",end="")
        print(" ")
