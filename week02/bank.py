# 

amount1 = input("Enter amount 1 (in cents) : ");
amount2 = input("Enter amount 2 (in cents) : ");

totalCents = int(amount1) + int(amount2);
totalEuro = totalCents/100;

print(f"The sum of {amount1} cents and {amount2} cents is : €{totalEuro}");