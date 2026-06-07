# Open file in write mode
file = open("output.txt", "w")

# Write data
file.write("Hello Python")

# Close file
file.close()

print("Data Written Successfully")

# Method 2: using with statement
with open("output.txt", "w") as file:

    file.write("Hello Python")

print("Data Written Successfully")