# Guess the number

# number of guess 10
# print number of guess left
# number of guess he took to finish
# print game over if guess are more then 10


number = 15
attemp = 10


while attemp > 0:
 attemp = attemp - 1
 input1 = int(input("Enter a number "))
 if input1 == 15:
    print("You win the game and number of attemp you took to finish is ",10-attemp)
    break
 elif input1 < 15:
    print("you enter lesser number please input greater number [ ",attemp ,"attemp left]")
 else:
    print("you enter greater number please input lesser number [ ",attemp ,"attemp left]")

if attemp == 0:
    print("Game over")

