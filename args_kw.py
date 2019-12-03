def fun(normal,*args,**kwargs):
    print(normal)

    for i in args:
        print(i)
    for key,value  in kwargs.items():
        print(f"{key} and {value}")

list = ["shubham","ankit","harshid"]
normal = "normal argument"
kwargs = {"hello": "world","ankit":"khunt"}
fun(normal, *list, **kwargs)