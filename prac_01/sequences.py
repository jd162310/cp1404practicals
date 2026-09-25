  # Show the even numbers from x to y
  # Show the odd numbers from x to y
  # Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
  # Exit the program
menu = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program"""
print(menu)
choice = int(input(""))
while choice != 4:
    x = int(input("please choose a value for x: "))
    y = int(input("please choose a value for y: "))
    if choice == 1:  # prints odd numbers
        if x % 2 != 0:
            if y % 2 != 0:
                print(list(range(x, y + 1, 2)))
            else:
                print(list(range(x, y, 2)))
        else:
            if y % 2 != 0:
                print(list(range(x + 1, y + 1, 2)))
            else:
                print(list(range(x + 1, y, 2)))
    elif choice == 2:  # prints even numbers
        if x % 2 != 0:
            if y % 2 != 0:
                print(list(range(x + 1, y, 2)))
            else:
                print(list(range(x + 1, y + 1, 2)))
        else:
            if y % 2 != 0:
                print(list(range(x, y, 2)))
            else:
                print(list(range(x, y + 1, 2)))
    elif choice == 3:  # prints the square of the numbers in a list
        square_numbers = []
        for i in range(x, y + 1):
            square_numbers.append(i ** 2)
        print(square_numbers)
    print(menu)
    choice = int(input(""))
print("closing program")