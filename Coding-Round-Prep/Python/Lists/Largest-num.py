nums = [10, 25, 5, 40, 15]

print(max(nums))

# Method 2: without built-in function
# Input list
nums = [10, 25, 5, 40, 15]

# Assume first element is largest
largest = nums[0]

# Traverse list
for num in nums:

    # Compare current element
    if num > largest:

        # Update largest
        largest = num

# Print result
print(largest)