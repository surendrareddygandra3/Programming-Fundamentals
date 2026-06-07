# Function definition
def total(*args):

    # Store sum
    result = 0

    # Traverse arguments
    for num in args:

        result += num

    return result


# Function call
print(total(10,20,30,40))