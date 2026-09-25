"""Password_stars"""
LENGHT = 10
def main():
    password = get_valid_password()
    print_stars(password)
def get_valid_password():
    """Gets a password from user with error checking"""
    password = input("enter a passward with a minimum lenght of 10 characters: ")
    while len(password) < LENGHT:  # error checking password lenght requirements
        password = input("invalid passward lenght, please enter password of lenght 10 or more: ")
    return password
def print_stars(password):  # prints '*' for lenght of the password
    print("Password: ")
    print('*' * len(password))
main()