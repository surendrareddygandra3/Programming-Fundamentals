# Function definition
def factorial(n):

    # Initial value
    fact = 1

    # Multiply numbers
    for i in range(1, n + 1):

        fact *= i

    # Return result
    return fact


# Function call
result = factorial(5)

print(result)