# Generator Function
def numbers():

    yield 1
    yield 2
    yield 3


# Iterate generator
for num in numbers():

    print(num)