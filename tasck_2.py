print("<---- Colculator ---->\n")
print("Enter a number from 1 to 5 where")
print("input 1 is +")
print("input 2 is -")
print("input 3 is *")
print("input 4 is /")
print("input 5 exiting the program")

while True:
    try:
        nb = int(input("Enter the operation number (1-5) -> "))
        if nb == 5:
            print("Exit . . . ")
            break
        if nb < 1 or nb > 4:
            print("Error input.")
            continue
        num1 = int(input("Enter the first number for the operation -> "))
        num2 = int(input("Enter the second number for the operation -> "))
        if nb == 1:
            res = num1 + num2
            print(f"Result: {num1} + {num2} = {res}")
        if nb == 2:
            res = num1 - num2
            print(f"Result: {num1} - {num2} = {res}")
        if nb == 3:
            res = num1 * num2
            print(f"Result: {num1} * {num2} = {res}")
        if nb == 4:
            if num2 == 0:
                print("Error! Division by zero is not possible")
            else:
                res = num1 / num2
                print(f"Result: {num1} / {num2} = {res}")
    except:
        print("Your Conclusion is incorrect :(")