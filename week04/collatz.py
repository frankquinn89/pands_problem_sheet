# collatz.py
# This program takes an input of a positive integer and outputs the value of the below logic.
# It calculates the next value by taking the current value and, if it is even, divides it by two and if it is odd, multiplies it by three and add one.
# It will stop once the value is 1.
# Author : Frank Quinn


def collatz_calc(value):
    numbers = []
    # Continue process until value = 1 
    while value != 1:
        # Print value each time
        numbers.append(value)
        # Check if value is even, if so, divide by 2
        if value % 2 == 0:
            value = value // 2
        else:
            # If value is odd, multiply by 3 and add 1
            value = (value * 3) + 1
    # Print list once loop is complete. Add 1 by default
    numbers.append(1)
    # print numbers on same line
    print(*numbers, sep=' ')




def validate_number():
    #loop to keep trying to get pos int
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 1:
                raise ValueError
            break
        #exception handling
        except ValueError:
            print("Error! Enter a positive integer.")
    # If number is valid, run the calc logic
    collatz_calc(num)


#run program and validate input number
validate_number()
