# Input list
nums = [1,2,2,3,3,4,5,5]

# Store seen numbers
seen = set()

# Store duplicates
duplicates = set()

# Traverse list
for num in nums:

    # If already seen
    if num in seen:
        duplicates.add(num)

    else:
        seen.add(num)

# Convert to list
print(list(duplicates))