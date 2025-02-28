print(" ***   multiplication table   *** ")
print("enter a number and you will see a multiplication table from 1 to 10\n")

while True:
    try:
        nb = int(input("Enter a number: "))
        break
    except:
        print("Invalid input! Please enter integer :(")


for i in range(1, 11):
    res = nb * i
    print(f"{nb} * {i} = {res}")