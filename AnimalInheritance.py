# Write a Python program that demonstrates inheritance by creating a base class Animal and 
# derived classes like Dog, Cat, etc., each with their specific behaviors.

# INPUT

# Base class
class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

# Base class
class dog(animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Derived class Cat
class cat(animal):
    def speak(self):
        print(f"{self.name} says Meow!")      

# Derived class Bird
class bird(animal):
    def speak(self):
        print(f"{self.name} says Tweet!")

x = dog("Buddy")
y = cat("Whiskers")
z = bird("Tweety")

x.speak()
y.speak()
z.speak()

# user will give input 
a = input("Enter the type of animal (dog/cat/bird): ").lower()
b = input("Enter the animal's name: ")

if a == "dog":
    pet = dog(b)
elif a == "cat":
    pet = cat(b)
elif a == "bird":
    pet = bird(b)
else:
    pet = animal(b)

pet.speak()
# OUTPUT
"""
Buddy says Woof!
Whiskers says Meow!
Tweety says Tweet!
Enter the type of animal (dog/cat/bird): dog
Enter the animal's name: buddy
buddy says Woof!

"""