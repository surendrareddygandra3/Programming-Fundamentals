# Parent Class
class Animal:

    def sound(self):

        print("Animal Sound")


# Child Class
class Dog(Animal):

    def sound(self):

        print("Bark")


# Create object
d1 = Dog()

# Call method
d1.sound()