while True:
    try:
        nb = int(input("input number - (0 to exit): "))
        if nb == 0:
            break
        if nb % 2 == 0:
            print("An even number.")
        else:
            print("An odd number.")
    except:
        print("Input Error :(")
