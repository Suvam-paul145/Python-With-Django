# Not parameterize =-> no arguement and no return type->
# add two no : 

import math as m
def add():
    a = int(input("Enter first no: "))
    b = int(input("Enter second no: "))
    c = a + b
    print(c)

add()

# factorial of number:
def factorial():
    n = int(input("Enter the number: "))
    print(m(n))

# arguement and no return type :
def greet(name):
    print("Hello " , name, "....")
    
greet("Suvam")

# add two no 
def add(a,b):
    a = int(input("Enter first no: "))
    b = int(input("Enter second no: "))
    c = (a + b)
    print(c)
add(5,36)

# factorial of number:
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)

# or using factoriAL FUNCTION 
    def factorial(n):
        fact = m.factorial(n)
n = int(input("Enter nop for factorial : "))
print(factorial(n))   