# Write a Python program to calculate the nth Fibonacci number using a function.

# INPUT
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter the position (n) in Fibonacci series: "))
r = fibonacci(n)
print(f"The {n}th Fibonacci number is: {r}")

# OUTPUT
"""
Enter the position (n) in Fibonacci series: 7
The 7th Fibonacci number is: 13

"""