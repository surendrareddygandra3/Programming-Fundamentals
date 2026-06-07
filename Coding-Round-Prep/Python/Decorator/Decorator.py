# Decorator Function
def my_decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper


# Apply Decorator
@my_decorator
def greet():

    print("Hello")


# Call Function
greet()