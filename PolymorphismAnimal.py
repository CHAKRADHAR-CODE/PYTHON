# Define a base class called Animal with a method make_sound(). Implement derived classes like Dog, Cat, and Bird that override 
# the make_sound() method to produce different sounds. Demonstrate polymorphism by calling the method on objects of different classes.

# INPUT

class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Derived class Dog
class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof!")

# Derived class Cat
class Cat(Animal):
    def make_sound(self):
        print("Cat says Meow!")

# Derived class Bird
class Bird(Animal):
    def make_sound(self):
        print("Bird says Tweet!")

# Demonstrating polymorphism
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.make_sound()
# OUTPUT
"""
Dog says Woof!
Cat says Meow!
Bird says Tweet!

"""