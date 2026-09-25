name = input("enter your name: ")
menu = ("""(H)ello
(G)oodbye
(Q)uit""")
print(menu)
choice = input("").upper()
while choice != "Q":
    if choice == "H":
        print("hello ", name)
    elif choice == "G":
        print("Goodbye ", name)
    else:
        print("Not a valid input")
    print(menu)
    choice = input("").upper()
print("you have quit the program")