# Open file
file = open("sample.txt", "r")

# Read content
content = file.read()

# Print content
print(content)

# Close file
file.close()

# Method 2: using with statement
with open("sample.txt","r") as file:

    content = file.read()

    print(content)