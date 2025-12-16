# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_total = 0
transport_total = 0
utilities_total = 0

for row in monthly_expenses:
    food_total += row[0]
    transport_total += row[1]
    utilities_total += row[2]

    week_total1 = sum(monthly_expenses[0])
    week_total2 = sum(monthly_expenses[1])
    week_total3 = sum(monthly_expenses[2])
    week_total4 = sum(monthly_expenses[3])

total_monthly_expenses = food_total + transport_total + utilities_total

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food_total)
print('Transport:',transport_total)
print('Utilities:',utilities_total)
print('Week 1:',week_total1)
print('Week 2:',week_total2)
print('Week 3:',week_total3)
print('Week 4:',week_total4)
print('---------------')
print('TOTAL:',total_monthly_expenses)