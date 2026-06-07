# Input number
n = 6

# Store sum of factors
total = 0

# Find factors
for i in range(1, n):

    if n % i == 0:

        total += i

# Check perfect number
if total == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")