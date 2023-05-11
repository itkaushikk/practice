year_in_deposit = 15
minimum_gm_gold_deposit = 10

print("value in current year:", 60000)
print("value of 10gm gold:", 60000)

gold_by_end_of_15 = minimum_gm_gold_deposit

for i in range(year_in_deposit):
    gold_by_end_of_15 = gold_by_end_of_15 + (gold_by_end_of_15 * 2.5/100)

print(gold_by_end_of_15)
print("value in 15 year:", 240000)
print(gold_by_end_of_15*240000/10)