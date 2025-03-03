print("Number of elements")
inputs = input("Enter the numbers separated by commas: ")
res = [item.strip() for item in inputs.split(",")]
print(f"the number of elements is == {len(res)}")