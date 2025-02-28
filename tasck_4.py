print("---- factorial ----")
print("---- You must enter a positive number starting from zero ----\n")

def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n - 1)
while True:
	try:
		nb = int(input("Enter a positive number: "))
		if nb < 0:
			print("ERROR\nYou entered a negative number.")
		else:
			print(f"The factorial {nb} is {factorial(nb)}")
			break
			
	except ValueError:
		print("Error input :( ")