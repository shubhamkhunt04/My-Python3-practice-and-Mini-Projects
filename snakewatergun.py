# s - snake
# w - water
# g - gun

# Rules :

#   user          computer            winner
#     s               w               user
#     w               g               user
#     g               s               user
#
#     w               s               computer
#     g               w               computer
#     s               g               computer
#
# if both same then draw

import random
level = 0
computerpoints = 0
userpoints = 0
while level < 10:
    list = ["s","w","g"]

    select = random.choice(list)
    level += 1
    user = input("Press s for Snake , Press w for Water , Press g for Gun :")
    if select  == user:
        print("draw")
    elif select == "s" and user == "w":
        computerpoints+=1
        print("Computer win")
        print("Computer points : ",computerpoints)
    elif select == "w" and user == "g":
        computerpoints+=1
        print("Computer win")
        print("Computer points : ",computerpoints)
    elif select == "g" and user == "s":
        computerpoints+=1
        print("Computer win")
        print("Computer points : ",computerpoints)


    elif user == "s" and select == "w":
        userpoints+=1
        print("You win")
        print("Your points : ",userpoints)
    elif user == "w" and select == "g":
        userpoints+=1
        print("You win")
        print("Your points : ",userpoints)
    elif user == "g" and select == "s":
        userpoints+=1
        print("You win")
        print("Your points : ",userpoints)
    else:
        print("Enter valid input")

print("********************************\n")
print("Your total points ",userpoints)
print("Computer total points ",computerpoints)

if userpoints == computerpoints:
    print("\n\n*** DRAW ***")
elif userpoints > computerpoints:
    print("\n\n*** YOU WIN ***")
else:
    print("\n\n*** COMPUTER WIN ***")


