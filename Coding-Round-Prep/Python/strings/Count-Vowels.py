# Input string
s = "surendra"

# Counter variable
count = 0

# Traverse each character
for ch in s:

    # Check vowel
    if ch in "aeiou":
        count += 1

# Print result
print(count)