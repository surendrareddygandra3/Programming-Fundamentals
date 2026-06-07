# Parent Class
class Animal:

    def sound(self):

        print("Animal Sound")


# Child Class
class Dog(Animal):

    pass


# Create object
d1 = Dog()

# Call parent method
d1.sound()