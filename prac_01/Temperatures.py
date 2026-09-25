  # Conversion of Celsius and Fahrenheit
print("Welcome to the temperature converter, type Q to quit")
user_input = input("Type C for Celsius and F for Fahrenheit: ")
while user_input.upper() != 'Q':
    temp_num = float(input("enter the numerical temperature value: "))
    if user_input.upper() == 'F':
        temp_convert = (temp_num - 32) / 1.8
        print(f"The temperature is {temp_convert:.2f} C")
    elif user_input.upper() == 'C':
        temp_convert = (temp_num * 1.8) + 32
        print(f"The temperature is {temp_convert:.2f} F")
    else:
        print("invalid")
    user_input = input("Type C for Celsius and F for Fahrenheit: ")
print("Bye bye")