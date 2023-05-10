file = open("ir.txt")

sum_inflation = 0
year_count = 0
for val in file:
    if val[-2] == "%":
        sum_inflation += float(val[-6:-2])
        year_count += 1
    elif val == "2000-01\n":
        break

print(year_count)
print(sum_inflation/year_count)