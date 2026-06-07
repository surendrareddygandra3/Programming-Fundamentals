# First dictionary
d1 = {'a':1,'b':2}

# Second dictionary
d2 = {'c':3,'d':4}

# Merge d2 into d1
d1.update(d2)

# Print result
print(d1)

# Method 2: using dictionary unpacking
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}

result = {**d1, **d2}

print(result)