f = open("shubham.txt")

print(f.tell())         # use to check the file handler(f) position
print(f.readline())

print(f.tell())
print(f.readline())

print(f.tell())
print(f.readline())

print(f.tell())

f.seek(0)               # use to reset the file handler(f)

print(f.readline())
print(f.tell())

f.close()