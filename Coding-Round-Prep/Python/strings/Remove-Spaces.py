# Input string
s = "hello world python"

# Remove spaces
result = s.replace(" ", "")

# Print result
print(result)


# Method 2: using loop
s = "hello world python"

result = ""

for ch in s:

    if ch != " ":
        result += ch

print(result)