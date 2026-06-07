# Parent Class 1
class Father:

    def father_method(self):

        print("Father Method")


# Parent Class 2
class Mother:

    def mother_method(self):

        print("Mother Method")


# Child Class
class Child(Father, Mother):

    pass


# Create Object
c = Child()

# Access methods
c.father_method()

c.mother_method()