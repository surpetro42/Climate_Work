print("---- Fibonacci ----")
print("---- You must enter a positive number starting from zero ----\n")

def Fibonacci(n):
    a = 0
    b = 1
    tmp = 1
    res = []
    for i in range(n):
        res.append(a)
        tmp = a + b
        a = b
        b = tmp
    print(res)

while True:
    try:
        nb = int(input("Enter a positive number: "))
        if nb > 0:
            Fibonacci(nb)
            break
    except ValueError:
        print("Error input :( ")
