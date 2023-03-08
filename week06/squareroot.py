# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root via the Newton Method
# Author: Frank Quinn

# Newton Method
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# Approach: The following steps can be followed to compute the answer:  
#1.Assign X to the N itself.
#2.Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
#3.Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue.
#4.If the calculated root comes inside the tolerance allowed then break out of the loop.
#5.Print the root.


def sqrt(num) :
    # Assuming the sqrt of num as num only
    x = num
    while True :
        # Calculate more closed x
        root = 0.5 * (x + (num / x))
        # Check for closeness / tolerance difference of root
        if (abs(root - x) < 0.0001) :
            break
        # Update root
        x = root

    approx_root = format(x, '.1f')
    print(f"The approximate square root of {num} is {approx_root}")
 


def main():
    #get input and validate
    while True:
        try:
            num = float(input("Enter a positive number: "))
            if num <= 0:
                raise ValueError
            break
        #exception handling
        except ValueError:
            print("Error! Enter a positive number.")
    # If number is valid, run the sqrt function
    root = sqrt(num)

#Run program
main()