with open("shubham.txt") as f:
    print(f.readlines())

# below code is also read file from starting position
f = open("shubham.txt")
print(f.readlines())
f.close()
