for i in range (0,6):
    for j in range(0,i):
        print("*",end = "")
    print("")

# using one for lopp 
for i in range(0,6):
    print("*" * i) # * is multiply by i times

# Make the pattern by using two for loop 
# *
# **
# ***
# ***
# **
# *

n = int(input("Enter the number of rows: "))
# it can take the string value if i don's type casting during input 

for i in range(0,n):
    print("*" * i)

for j in range(n-1,0,-1):
    print("*" *j)

# Make the pattern by using one for loop 
