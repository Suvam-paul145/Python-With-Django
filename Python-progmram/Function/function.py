# Not parameterize =-> no argument and no return type->

import math as m

# add two no :
def add():
    a = int(input("Enter first no: "))
    b = int(input("Enter second no: "))
    c = a + b
    print(c)

add()

# factorial of number:
def factorial():
    n = int(input("Enter the number: "))
    print(m.factorial(n))

# argument and no return type :
def greet(name):
    print("Hello ", name, "....")

greet("Suvam")

# add two no 
def add(a, b):
    c = a + b
    print(c)

add(5, 36)

# factorial of number:
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

# or using factorial FUNCTION 
def factorial_using_lib(n):
    fact = m.factorial(n)
    print(fact)

n = int(input("Enter number for factorial: "))
factorial(n)