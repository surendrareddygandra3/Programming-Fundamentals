# Open file
with open("sample.txt", "r") as file:

    # Read file content
    content = file.read()

    # Split into words
    words = content.split()

    # Count words
    print(len(words))


# Method 2: line by line
count = 0

with open("sample.txt", "r") as file:

    for line in file:

        words = line.split()

        count += len(words)

print(count)