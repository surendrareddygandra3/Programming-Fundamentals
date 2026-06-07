# Recursive Fibonacci Function
def fib(n):

    # Base Cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Recursive Call
    return fib(n-1) + fib(n-2)


print(fib(6))