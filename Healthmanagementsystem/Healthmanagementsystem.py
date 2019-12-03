def choice_exordie():
    print("(1) Exercise")
    print("(2) Diet")

def exercisesuggestion():
    print("*** Note your Exercise ***")
    print("*** Press q for Exit ***")

def dietsuggestion():
    print("*** Note your Diet ***")
    print("*** Press q for Exit ***")


def getdate():
    import datetime
    return datetime.datetime.now()


def writing():             # Log the data
    str1 = ""
    date = str(getdate())  # convert date object into string ,with the help of str() function.
    while str1 != "q":
        str1 = input()
        if (str1 == 'q'): break  # because q not write in file
        f.write(" => [ " + date + " ] --: ")
        f.write(str1+"\n")
    f.close()


def reading():             # Retrieve the data
    print(f.read())
    f.close()



# Run- Debug here
print("********** HEALTH MANAGEMENT SYSTEM **********")
print("Enter your choice ")
print("(1) Log your data ")     # Log means data entry with time stamp
print("(2) Retrieve your data ")
input1 = int(input())

print("(1) Shubham")
print("(2) Ankit")
print("(3) Harshid")
client_id = int(input("Enter your client id "))

if input1 == 1:
    if client_id == 1:
        choice_exordie()
        choice = int(input())
        if choice == 1:
            exercisesuggestion()
            f = open("Exercise1.txt", "a+")         # a+ : read,write and append mode
            writing()
        elif choice == 2:
            dietsuggestion()
            f = open("Diet1.txt", "a+")
            writing()
        else:
            print("Enter valid choice")

    elif client_id == 2:
        choice_exordie()
        choice = int(input())
        if choice == 1:
            exercisesuggestion()
            f = open("Exercise2.txt", "a+")
            writing()
        elif choice == 2:
            dietsuggestion()
            f = open("Diet2.txt", "a+")
            writing()
        else:
            print("Enter valid choice")

    elif client_id == 3:
        choice_exordie()
        choice = int(input())
        if choice == 1:
            exercisesuggestion()
            f = open("Exercise3.txt", "a+")
            writing()
        elif choice == 2:
            dietsuggestion()
            f = open("Diet3.txt", "a+")
            writing()
        else:
            print("Enter valid choice")



elif input1 == 2:
    if client_id == 1:
        choice_exordie()
        input2 = int(input())
        if input2 == 1:
            f = open("Exercise1.txt")
            reading()
        elif input2 == 2:
            f = open("Diet1.txt")
            reading()
        else:
            print("Enter valid choice")

    elif client_id == 2:
        choice_exordie()
        input2 = int(input())
        if input2 == 1:
            f = open("Exercise2.txt")
            reading()
        elif input2 == 2:
            f = open("Diet2.txt")
            reading()
        else:
            print("Enter valid choice")

    elif client_id == 3:
        choice_exordie()
        input2 = int(input())
        if input2 == 1:
            f = open("Exercise3.txt")
            reading()
        elif input2 == 2:
            f = open("Diet3.txt")
            reading()
        else:
            print("Enter valid choice")




