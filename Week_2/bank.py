# 

amount1 = input("Enter amount 1 (in cents) : ");
amount2 = input("Enter amount 2 (in cents) : ");

totalCents = int(amount1) + int(amount2);
totalEuro = totalCents/100;

result = "The sum of {} cents and {} cents is : €{}".format(amount1, amount2, totalEuro);
print(result);
