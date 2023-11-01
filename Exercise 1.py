import random

n = int(input("Enter the maximum capacity of your list:"))
my_list = []

for i in range(n):
    z = (random.randint(1,100))
    if z not in my_list:
        my_list.append(z)

for i in range(len(my_list)):
    print(my_list[i], end=" ")