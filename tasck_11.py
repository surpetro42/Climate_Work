nb = input("enter a number: ")
if nb.isdigit():
    res = sum(int(digit) for digit in nb)
    print(f"the sum of the digits {nb} == {res}")
else:
    print(f"Error: Enter a positive integer.")
