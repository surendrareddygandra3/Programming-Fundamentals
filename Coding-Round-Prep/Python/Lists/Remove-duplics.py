# Input list
nums = [1, 2, 2, 3, 4, 4, 5]

# Convert list to set
unique_nums = list(set(nums))

# Print result
print(unique_nums)


# Method 2: without using set
nums = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in nums:

    if num not in result:
        result.append(num)

print(result)