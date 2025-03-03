print("Enter the numbers to find out their sum.")
inputs = (input("enter the numbers: "))
arr = [int(item.strip()) for item in inputs.split(" ")]
res = sum(arr)
print(f"the sum of the elements is equal to -> {res}")
