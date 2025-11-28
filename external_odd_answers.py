# Question 1:
'''
a) Write a program that asks the user for a weight in kilograms and converts it to pounds. There
are 2.2 pounds in a kilogram.
A) 
code: 
'''
kg = float(input("Enter The weight in Kilograms : "))
print(f"Weight in Pounds : {kg*2.2:.1f}")

'''
🧠 Explanation
    kg * 2.2 converts kilograms to pounds.
    The format specifier :.1f means:
        👉 show 1 digit after the decimal point (you can change it to .2f for 2 digits).
    You used :1f, which is not wrong but doesn’t fix decimal places — it sets field width.
    .1f or .2f is what you need for proper decimal formatting.


Sample Output :
Enter the weight in Kilograms: 50
Weight in Pounds: 110.0
'''

'''
b) Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89
A) 
code: 
'''
for i in range(8,90,3):
    print(i,end=" ")

'''
🧠 Explanation
    range(8, 90, 3)
        Starts from 8
        Goes up to (but not including) 90
        Increments by 3 each time
    The end=" " in print() keeps the numbers on the same line, separated by spaces.


Sample Output :
8 11 14 17 20 23 26 29 32 35 38 41 44 47 50 53 56 59 62 65 68 71 74 77 80 83 86 89
'''

#------------------------------------------------------------------------------------------------

# Question 3:
'''
Write a python program to calculate the nth Fibonacci number using a function. (Recursion)

code: 
'''
def fib(n):
    if n<=0:
        return "Invalied Input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input("Enter The value n : "))
print(f"the {n}th Fibonacci Series is : {fib(n)}")

'''
🧠 Explanation
    The function fibonacci(n) calls itself recursively:
        Base cases:
            n == 1 → 0
            n == 2 → 1
        Recursive case:
            fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    The recursion continues until it reaches the base cases.
    The function returns the nth Fibonacci number.


Sample Output :
Enter The value n : 7
the 7th Fibonacci Series is : 8
'''

#------------------------------------------------------------------------------------------------

# Question 5:
'''
Write a Python program that demonstrates inheritance by creating a base class Animal
and derived classes like Dog, Cat, etc., each with their specific behaviors.

code: 
'''
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "Some Generic Sounds"
class dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class cat(Animal):
    def speak(self):
        return f"{self.name} saya Meow!"
d=dog("Maggie")
c=cat("mafi")

print(d.speak())
print(c.speak())

'''
🧠 Explanation
    Animal (Base class) — defines a constructor (__init__) and a general method speak().
    dog and cat (Derived classes) — inherit from Animal and override the speak() method.
    When you call d.speak() or c.speak(), Python uses the child class version (method overriding).

Sample Output :
Maggie says Woof!
Mafi says Meow!

'''

#------------------------------------------------------------------------------------------------

# Question 7:
'''
Write a python program that demonstrates error handling using try-except block to handle
division by zero.

code: 
'''
try:
    x = int(input("Enter Numerator : "))
    y = int(input("Enter Denominator : "))
    print(f"Result : {x/y}")
except ZeroDivisionError:
    print("Error : Division By Zero Not Allowed")
except ValueError:
    print("Error : Please Enter The valid numeri Values")

'''
🧠 Explanation
    The code inside the try block is executed normally.
    If the denominator b is 0, Python raises a ZeroDivisionError.
        The program then jumps to the corresponding except ZeroDivisionError: block.
    The ValueError block handles invalid (non-numeric) inputs gracefully.
    This prevents the program from crashing.

Sample Output :
Enter numerator: 10
Enter denominator: 2
Result: 5.0
'''

#------------------------------------------------------------------------------------------------

# Question 9:
'''
Write a NumPy program using NumPy methods - max, min, argmax, argmin, argmax,
repr, count, bincount, unique.
To extract all numbers from a given array which are less and greater than a
specified number.

code: 
'''
import numpy as np
x = np.array(list(map(int,input("Enter The Values : ").split())))
print(f"Array : {repr(x)}")
print(f"Max Number : {np.max(x)}")
print(f"Min Number : {np.min(x)}")
print(f"Index of Max value : {np.argmax(x)}")
print(f"Index of Min value : {np.argmin(x)}")
print(f"Count of 5 in array : {np.count_nonzero(x==5)}")
print(f"Bin Count : {np.bincount(x)}")
print(f"Unique : {np.unique(x)}")


y = int(input("Enter The Number : "))
print(f"Number Less Than {y} are : {x[x<y]}")
print(f"Number More Than {y} are : {x[x>y]}")

'''
Sample Output :
Enter The Values : 2 5 7 3 9 5 7 2 3 9 1 5
Array : array([2, 5, 7, 3, 9, 5, 7, 2, 3, 9, 1, 5])
Max Number : 9
Min Number : 1
Index of Max value : 4
Index of Min value : 10
Count of 5 in array : 3
Bin Count : [0 1 2 2 0 3 0 2 0 2]
Unique : [1 2 3 5 7 9]
Enter The Number : 5
Number Less Than 5 are : [2 3 2 3 1]
Number More Than 5 are : [7 9 7 9]
'''

#------------------------------------------------------------------------------------------------

# Question 11:
'''
Pandas Data Series: Write a Pandas program to create and display a one -dimensional arraylike 
object containing an array of data using Pandas module

code: 
'''
import pandas as pd

x = list(map(int, input("Enter the values: ").split()))
y = pd.Series(x)
print(y)


'''
🧠 Explanation
    input() → takes user input as a string.
    map(int, input().split()) → splits the input into separate numbers and converts each to an integer.
    pd.Series(x) → converts the list into a Pandas Series (a 1D labeled array).
    print(y) → displays the Series with automatically generated index labels (0, 1, 2, ...).

Sample Output :
Enter the values: 10 20 30 40 50
0    10
1    20
2    30
3    40
4    50
dtype: int64
'''

#------------------------------------------------------------------------------------------------

# Question 13:
'''
Pandas Data Frames :
Consider sample Python dictionary data and list labels :
Exam_data = {‘name: [‘Anastasia’, ‘Dima’, ‘Katherine’, ‘James’, ‘Emily’ ‘Michael’,
Matthew’, ‘Laura’, ‘Kevin’, ‘Jonas’],
‘score’ : [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
‘attempts’:[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
‘qualify’:[‘yes’, ‘no’, ‘yes’, ‘no’, ‘no’, ‘yes’, ‘yes’, ‘no’, ‘no’, ‘yes’ ]}
Labels = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘I’, ‘j’].
Write a Pandas program to create and display a DataFrame from a specified dictionary data
which has the index labels.

code: 
'''
import numpy as np
import pandas as pd
Exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
Labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

x = pd.DataFrame(Exam_data,index = Labels)
print(x)


'''
🧠 Explanation
    Dictionary Exam_data holds all column data:
    name, score, attempts, qualify
    Labels list defines the custom row indices (a–j).
    pd.DataFrame(Exam_data, index=Labels) creates the DataFrame with given data and labels.
    np.nan represents missing values (Not a Number).

Sample Output :
        name  score  attempts qualify
a  Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c  Katherine   16.5         2     yes
d      James    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes
'''


#------------------------------------------------------------------------------------------------

# Question 15:
'''
Pandas Data Frames :
Consider sample Python dictionary data and list labels :
Exam_data = {‘name: [‘Anastasia’, ‘Dima’, ‘Katherine’, ‘James’, ‘Emily’ ‘Michael’,
Matthew’, ‘Laura’, ‘Kevin’, ‘Jonas’],
‘score’ : [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
‘attempts’:[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
‘qualify’:[‘yes’, ‘no’, ‘yes’, ‘no’, ‘no’, ‘yes’, ‘yes’, ‘no’, ‘no’, ‘yes’ ]}
Labels = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘I’, ‘j’].
Write a Pandas program to insert a new column in existing DataFrame.

code: 
'''
import numpy as np
import pandas as pd
Exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
Labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

x = pd.DataFrame(Exam_data,index = Labels)
print("Original DataFrame : ")
print(x)

x["age"]=[18,20,19,2,21,23,20,18,19,22]
print("DataFrame after adding : ")
print(x)


'''
🧠 Explanation
    A DataFrame df is created using the provided dictionary Exam_data and custom index labels.
    A new column ‘age’ is added directly by assignment:
        df['age'] = [...]
    This creates a new column in the DataFrame with the given list of values.
    Finally, the updated DataFrame is printed.

Original DataFrame : 
        name  score  attempts qualify
a  Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c  Katherine   16.5         2     yes
d      James    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes
DataFrame after adding :
        name  score  attempts qualify  age
a  Anastasia   12.5         1     yes   18
b       Dima    9.0         3      no   20
c  Katherine   16.5         2     yes   19
d      James    NaN         3      no    2
e      Emily    9.0         2      no   21
f    Michael   20.0         3     yes   23
g    Matthew   14.5         1     yes   20
h      Laura    NaN         1      no   18
i      Kevin    8.0         2      no   19
j      Jonas   19.0         1     yes   22
'''

#------------------------------------------------------------------------------------------------

# Question 17:
'''
Create a series of plots to analyze a given dataset.

code: 
'''
import pandas as pd
import matplotlib.pyplot as plt

x = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Marks':[80,65,90,70,85],
    'Attempts' : [1,3,2,2,1],
    'Pass': ['Yes', 'No', 'Yes', 'No', 'Yes']
}
y = pd.DataFrame(x)
print("Dataset:\n", y)

fig, z = plt.subplots(2,2,figsize = (9,7))
fig.suptitle("Student Data Analyis",fontsize = 14,fontweight = 'bold')

z[0,0].bar(y['Name'],y['Marks'])
z[0,0].set_title("Marks Of Students")
z[0,0].set_xlabel("NAME")
z[0,0].set_ylabel("Marks")

p = y['Pass'].value_counts()
z[0,1].pie(p,labels = p.index)
z[0,1].set_title("Pass/Fail ratio")

z[1,0].plot(y['Attempts'],y['Marks'],marker = 'o')
z[1,0].set_title("Attempt vs Marks")
z[1,0].set_xlabel('Attempt')
z[1,0].set_ylabel('Marks')

z[1,1].scatter(y['Attempts'],y['Marks'],marker = 'o')
z[1,1].set_title("Marks Analysis")
z[1,1].set_xlabel('Attempt')
z[1,1].set_ylabel('Marks')

plt.tight_layout(rect = [0,0,1,0.95])
plt.show()

#------------------------------------------------------------------------------------------------

# Question 19:
'''
Visualize time-series data and customize axis labels and date formats.

code: 
'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.date_range(start = '2025-01-01',periods = 7,freq = 'D')
sales = [110,120,130,140,150,160,170]

x = pd.DataFrame({'date':data,'sales':sales})
print(x)

plt.figure(figsize = (8,5))
plt.plot(x["date"],x["sales"],marker = 'o')
plt.title("time-series")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation = 45)
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------------------------------