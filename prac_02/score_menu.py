"""score menu"""
def main():
    score = get_score()
    print_menu()
    choice = input().upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            print_grade(score)
        elif choice == 'S':
            print_stars(score)
        print_menu()
        choice = input().upper()
    print("farewell")

def print_menu():
    """prints main menu message"""
    print("""(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit""")

def get_score():
    """gets the user to input a score"""
    score = float(input("Enter score between 0-100: "))
    while 0 > score or 100 < score:
        score = float(input("invalid score, between 0-100 is valid: "))
    return score

def print_grade(score):
    """Prints what tier the grade is"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def print_stars(score):
    """prints a number of stars based on the score number"""
    print('*' * int(score))

main()