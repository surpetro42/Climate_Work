def is_armstrong(num):
    strnum = str(num)
    lennum = len(strnum)

    res = sum(int(digit) ** lennum for digit in strnum)
    return res == num

inputs = input("Enter a number: ")
if inputs.isdigit():
    nb = int(inputs)
    if is_armstrong(nb):
        print(f"{nb} — This number Armstrong.")
    else:
        print(f"{nb} — This number not Armstrong.")
else:
    print("ERROR input :(")