def second_largest(arr):
    unique_nb = list(set(arr))
    if len(unique_nb) < 2:
        return None
    unique_nb.sort(reverse=True)
    return unique_nb[1]

print("the second maximum number.")
arr = [1,2,11,56,45,45,120,2,37,4,68,9]
res = second_largest(arr)
if res is not None:
    print(f"The largest number in the list -> {res}")
else:
    print(f"Error :(")