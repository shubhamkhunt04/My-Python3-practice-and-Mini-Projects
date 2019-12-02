import random
random_number1 = random.randint(5, 10)      # only integer

random_number2 = random.random() * 10       # between 1 to 10

print(random_number1)
print(random_number2)

list = ["shubham","ankit","harshid"]

select = random.choice(list)

print(select)