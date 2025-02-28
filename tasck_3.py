import random
nb = random.randint(1, 10)
print("---------- A random number from 1 to 10 was generated. Your task is to find this figure. ----------\n")

while True:
    try:
        inputn = int(input("Enter a number from 1 to 10 to find the generated number: "))
        if inputn < 1 or inputn > 10:
            print(" - - - Your input does not follow the rules of the code - - - ")
        if inputn == nb:
            print("*** Congratulations! You found the generated number ***")
            break
        elif inputn == nb - 1:
            print("You're very close.")
        elif inputn == nb + 1:
            print("You're very close.")
        elif inputn == nb + 2 or inputn == nb + 3:
            print("You're close.")
        elif inputn == nb - 2 or inputn == nb - 3:
            print("You're close.")
        elif inputn == nb + 4 or inputn == nb + 5:
            print("You can do better")
        elif inputn == nb - 4 or inputn == nb - 5:
            print("You can do better")
        else:
            print("I believe you")
    except:
        print("Error input :(")