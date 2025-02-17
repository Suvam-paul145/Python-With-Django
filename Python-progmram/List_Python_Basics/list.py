# write a code to print the list of elements, tuples and dictionary in python

# variable argument function:

list = ['suvam', 'JISCE', 1010]
# Removed unnecessary input and loop
for item in list:
    print(item)

# create the list in ascending order

list = [1, 92, 3, 4, 55, 6, 70, 8, 9, 10]
sorted_list = sorted(list)
print(sorted_list)

# print the list in reverse order
reverse_list = sorted_list[::-1]
print(reverse_list)

# tuple

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_from_tuple = list(t)
list_from_tuple.reverse()
print(list_from_tuple)


