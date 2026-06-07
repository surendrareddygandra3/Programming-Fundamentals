# Input string
s = "banana"

# Empty dictionary
freq = {}

# Traverse each character
for ch in s:

    # Check if character already exists
    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1

# Print result
print(freq)

# Method 2: using get() method
s = "banana"

freq = {}

for ch in s:

    freq[ch] = freq.get(ch, 0) + 1

print(freq)