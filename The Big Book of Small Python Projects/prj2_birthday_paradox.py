import random

print("how many birthdays i need to generate")
birthdays = int(input("> "))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

matching_birthdays = 0
count = 0
while count < 100_000:
    generate_birthdays = []
    
    for i in range(birthdays):
        pick_month = random.choice(months)
        
        if pick_month in ["Feb"]:
            pick_date = random.randint(1,29)
        elif pick_month in ["Apr", "Jun", "Sep", "Nov"]:
            pick_date = random.randint(1,30)
        else:
            pick_date = random.randint(1,31)
        
        full_date = pick_month + " " + str(pick_date)
        generate_birthdays.append(full_date)
        
    for date in generate_birthdays:
        if generate_birthdays.count(date) > 1:
            matching_birthdays += 1
            break
    
    count += 1

percentage_val = (matching_birthdays/100_000)*100
print(percentage_val)        