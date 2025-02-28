res = 0

while(1):
    s = input("enter 1 or 2: ")
    if s == '1' or s == '2':
        nb = int(s)
        if nb == 2:
            break
        res += nb
    else:
        print("You didn't enter anything.")
print("The sum of your inputs == ", res)
