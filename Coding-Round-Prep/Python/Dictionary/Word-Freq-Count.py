# Input sentence
text = "I love python I love AI"

# Convert sentence into words
words = text.split()

# Empty dictionary
freq = {}

# Count frequency
for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Print result
print(freq)