# collatz.py
# This program takes an input of a positive integer and outputs the value of the below logic.
# It calculates the next value by taking the current value and, if it is even, divides it by two and if it is odd, multiplies it by three and add one.
# It will stop once the value is 1.
# Author : Frank Quinn


def calc_value(value):
    # Continue process until value = 1 
    while value != 1:
        # Print value each time
        print(value)
        # Check if value is even, if so, divide by 2
        if value % 2 == 0:
            value = value // 2
        else:
            # If value is odd, multiply by 3 and add 1
            value = (value * 3) + 1
    # Print value once loop is complete       
    print(value)


def get_number():
    #loop to keep trying to get pos int
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if not isinstance(num, int):
                raise ValueError
            break
        #exception handling
        except ValueError:
            print("Error! Enter a positive integer.")
    # If number is valid, run the calc logic
    calc_value(num)


#run program
get_number()
