# Write a Python program that demonstrates error handling using the try-except block to handle division by zero.

# INPUT

try :
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    r = x/y
    print("Result:",r)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

# OUTPUT
"""
Enter numerator: 8
Enter denominator: 0
Error: Division by zero is not allowed.

"""