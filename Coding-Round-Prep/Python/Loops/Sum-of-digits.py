n = 1234

total = 0

for digit in str(n):
    total += int(digit)

print(total)


# Method 2: without converting to string
# Input number
n = 1234

# Store sum
total = 0

# Loop until number becomes 0
while n > 0:

    # Get last digit
    digit = n % 10

    # Add digit to total
    total += digit

    # Remove last digit
    n = n // 10

# Print result
print(total)