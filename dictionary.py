# Dictionary is nothing but key value pairs

dic = { 1:"one",2:"two",3:"three",4:"four",5:"five"}
print(dic)
print(dic[1])

dic1=dic
del dic[5]      # delete 5 in dic1 and dic
print(dic)

dic2 = dic.copy()
del dic[3]      # delete 3 in dic only
print(dic2)
print(dic)

dic.update({6:"six"})
print(dic)

print(dic.keys())
print(dic.items() )