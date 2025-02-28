print("*** Simple and complex numbers *** \n")

while True:
    try:
        inputn = int(input("Enter the number: "))
        break
    except:
        print("ERROR!\ninput incorect")
if inputn % 2 == 0:
    print(f"{inputn} Is not a prime number")
else:
    print(f"{inputn} Is a prime number")