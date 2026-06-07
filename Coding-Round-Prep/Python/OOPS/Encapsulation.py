# Employee Class
class Employee:

    def __init__(self, salary):

        # Private variable
        self.__salary = salary

    # Getter Method
    def get_salary(self):

        return self.__salary


# Create object
e1 = Employee(50000)

# Access through method
print(e1.get_salary())