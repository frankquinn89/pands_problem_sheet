# bank.py
# This program outputs the sum of 2 inputs (in cents) into Euro format.
# Author: Frank Quinn

amount1 = input("Enter amount 1 (in cents) : ")
amount2 = input("Enter amount 2 (in cents) : ")

#add the 2 values and format to 2 decimal places
totalCents = int(amount1) + int(amount2)
totalEuro = format(totalCents/100, '.2f')

print(f"The sum of {amount1} cents and {amount2} cents is : €{totalEuro}")