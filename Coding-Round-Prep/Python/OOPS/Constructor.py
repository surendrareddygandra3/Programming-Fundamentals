# Create class
class Student:

    # Constructor
    def __init__(self, name, age):

        self.name = name
        self.age = age


# Create object
s1 = Student("Surendra", 23)

# Print values
print(s1.name)
print(s1.age)