# Original dictionary
d = {
    'a':1,
    'b':2,
    'c':3
}

# Empty dictionary
inverted = {}

# Traverse dictionary
for key, value in d.items():

    # Swap key and value
    inverted[value] = key

# Print result
print(inverted)


# Method 2: using dictionary comprehension
d = {
    'a':1,
    'b':2,
    'c':3
}

inverted = {value:key for key,value in d.items()}

print(inverted)
