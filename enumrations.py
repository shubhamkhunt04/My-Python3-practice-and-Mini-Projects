list = ["one","two","three","four"]

i = 1
for item in list:
    if i % 2!=0:
        print(item)
    i+=1


# use of enumerate 
for index , item in enumerate(list):
    if index % 2 ==0:
        print(item)