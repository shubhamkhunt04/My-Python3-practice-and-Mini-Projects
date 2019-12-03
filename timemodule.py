import  time

start = time.time()
i = 0
while i < 1000:
    print("hello shubham")
    i+=1
print("while loop execution time : ",time.time() - start ,"in secend")

start2 = time.time()
for i in range(1000):
    print("hello ankit")
print("for loop execution time : ", time.time() - start2, "in secend")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)