# First list
list1 = [1,2,3,4]

# Second list
list2 = [3,4,5,6]

# Store common elements
common = []

# Traverse first list
for num in list1:

    # Check if present in second list
    if num in list2:

        common.append(num)

# Print result
print(common)