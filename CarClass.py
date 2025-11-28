# Write a Python program that defines a Car class with attributes like make, model, and year, 
# and methods like start() to start the car and stop() to stop it.

# INPUT
class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} has stopped.")

x = input("Enter car make: ")
y = input("Enter car model: ")
z = input("Enter car year: ")

mycar = car(x,y,z)
mycar.start()
mycar.stop()

# OUTPUT
"""
Enter car make: Honda
Enter car model: Civic
Enter car year: 2021
The 2021 Honda Civic is starting.
The 2021 Honda Civic has stopped.

"""