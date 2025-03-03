import math

nb1_input = input("Enter the first number: ")
nb2_input = input("Enter the second number: ")

if nb1_input.isdigit() and nb2_input.isdigit():
    nb1 = int(nb1_input)
    nb2 = int(nb2_input)
    res = math.gcd(nb1, nb2)
    print(f"The Greatest Common Divisor of {nb1} and {nb2} is {res}")
else :
    print("ERROR input :(")
