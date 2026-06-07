# Input number
n = 153

# Save original number
original = n

# Store sum
total = 0

# Process each digit
while n > 0:

    digit = n % 10

    total += digit ** 3

    n = n // 10

# Check Armstrong
if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")