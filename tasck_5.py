print("*** Palindrome ***")
print("A palindrome is a word or phrase that reads the same\nway both from left to right and from right to left.")

string = input("Enter words or text that is a palindrome: -> ").strip()

def palindrome(string):
    string = string.lower()
    return string == string[::-1]

print("\n")
if palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
