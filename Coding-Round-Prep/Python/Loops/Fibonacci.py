# Number of terms
n = 10

# First two numbers
a = 0
b = 1

# Loop n times
for i in range(n):

    # Print current number
    print(a, end=" ")

    # Generate next Fibonacci number
    a, b = b, a + b