# Input String
s = "hello"

# Reverse the string using slicing
reversed_string = s[::-1] # start-end-step

# Print the reversed string
print(reversed_string)

# Method 2: without slicing
s= "HI"
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string
print(reversed_string)

# # Method 3: using built-in function
s = "hello"
reversed_string = ''.join(reversed(s))
print(reversed_string)
