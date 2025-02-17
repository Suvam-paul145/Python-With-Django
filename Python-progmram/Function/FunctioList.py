def list():
    li = []
    n1 = int(input("Enter the left bound"))
    n2 = int(input("Enter the right bound"))
    for i in range(n1,n2):
        li.append(i)
    print(li)

# touple format of a function
def fun(*variable):
    print(fun(type(variable)))


# sum of the variable using the touple format 

def sum(*variable):   # here the variable is the name of the touple
    sum = 0 
    for  i in variable:
        sum = sum +i
    print(sum)

sum(1,2,3,4,5,6,7,8,9,10)
sum (1,5,8)