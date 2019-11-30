f = open("shubham.txt")

print(f.readline() ,end="")     # print only first line

for line in f:          # print second line because f points to new line
    print(line , end="")

"""
OUTPUT : 

shubham is a good boy.
practice makes you perfect.
"""