# sum of series : 1/3 + 1/5 + 1/7 + 1/9 + .....
n = int(input("Enter the number of elements you want to sum for odd series: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / (2 * i + 1)
print(sum)