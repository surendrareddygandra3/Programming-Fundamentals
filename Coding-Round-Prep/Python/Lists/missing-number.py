# Input list
nums = [1, 2, 3, 5]

# Total numbers should be 5
n = 5

# Expected sum
expected_sum = n * (n + 1) // 2

# Actual sum
actual_sum = sum(nums)

# Missing number
missing = expected_sum - actual_sum

print(missing)


# Method 2: 
nums = [1,2,3,5]

for i in range(1,6):

    if i not in nums:
        print(i)