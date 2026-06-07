try:

    num = 10

    result = num / 0

    print(result)

except ZeroDivisionError:

    print("Cannot divide by zero")


# Method 2: using exception object
try:

    print(10/0)

except ZeroDivisionError as e:

    print(e)

# Method 3: using finally block
try:

    print(10/0)

except ZeroDivisionError:

    print("Error")

finally:

    print("Always Executes")