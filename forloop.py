list = ["shubham" , "khunt" , "git" ,"hub"]

for item in list:
    print(item)


list2 = [ ["shubham",1] , ["khunt",2] , ["git" ,3] ,["hub" ,4]]
for item,number in list2:
    print(item , number)

dict1 = dict(list2)     # typecast
for item,number in dict1.items():
    print(item , number)


list3 = [ 1, "hello", "shubham" , 5 , 6 , 7 , 1 , 2 ,"world"]

for item in list3:
    if str(item).isnumeric() and item < 6:
        print(item)



