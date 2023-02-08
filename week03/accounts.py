#accounts.py
# This program takes an input account number and outputs the account number, hiding all but the last 4 characters
# Author: Frank Quinn

acc_num = input("Enter Account Number: ")

#I am assuming the length of the account number is greater than 4, otherwise all characters will be hidden
while len(acc_num) < 5:
    acc_num = input("Account Number must contain at least 5 characters. Try again: ")

#replace all charatcers with X, remove last 4 X characters and append last 4 actual characters
acc_num ='X'*(len(acc_num) - 4) + acc_num[-4:]

print(acc_num)