print("Mximum number.")
inputs = input("enter 3 numbers: ")
arr = [int(item.strip()) for item in inputs.split(" ") if item.strip().isdigit()]
if len(arr) == 3:
    largest = max(arr)
    print(f"The largest number in the list -> {largest}")
else:
    print(f"Error: incorrect quantity.")