in_years = 15
per_year = 10
amount = 100000

for i in range(4):
    amount = amount + ((amount * per_year/100)/4)

print(amount)