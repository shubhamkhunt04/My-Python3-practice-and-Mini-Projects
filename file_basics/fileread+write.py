f = open("shubham.txt" , "r+")

print(f.read())

totalcharacter = f.write("\nhello world")

print(totalcharacter)

print(f.readline())  # read hello world

f.close()