# Input String 
s = "madam"

# Check if the string is equal to its reverse
if s == s[::-1]:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")


# Method 2: without slicing
s = "madam"
reversed_string = ""

for char in s:
    reversed_string = char + reversed_string

if s == reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome")