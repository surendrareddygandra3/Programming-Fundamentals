# Input number
n = 13

# Assume prime
is_prime = True

# Check divisibility
for i in range(2, n):

    if n % i == 0:

        is_prime = False
        break

# Print result
if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")