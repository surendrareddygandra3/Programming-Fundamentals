# Input list
nums = [10, 25, 5, 40, 15]

# Sort list
nums.sort()

# Print second largest
print(nums[-2])


# Method 2: without sorting
nums = [10, 25, 5, 40, 15]

largest = second = float('-inf')

for num in nums:

    if num > largest:

        second = largest
        largest = num

    elif num > second and num != largest:

        second = num

print(second)