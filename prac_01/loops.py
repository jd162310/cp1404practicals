for i in range(1, 21, 2):
    print(i, end=' ')
print()  # loop for printing the odd numbers between 0-20

  # loop for counting in 10s from 0-100
for i in range(0, 100, 10):
    print(i, end=' ')
print()

  # loop for counting down from 20-1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

  # loop for printing a number of * based of the user input
number_stars = int(input("how many stars to print: "))
for i in range(1, number_stars + 1):
    print('*', end='')
print()

   # loop for printing a increasing number of stars from user input
for i in range(1, number_stars + 1):
    print(i * '*')
print()
