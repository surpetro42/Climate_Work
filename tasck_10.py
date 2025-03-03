print("enter a string if you want to know the number of capital letters.")
string = input("input: ")
vowels = "aeiouAEIOU"
count = count = sum(1 for elem in string if elem in vowels)
print(f"the number of uppercase letters per line -> {count}")