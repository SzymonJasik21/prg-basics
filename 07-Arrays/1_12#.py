categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = expenses[0]
most_expensive_category = categories[0]

for i in range(len(expenses)):
    if expenses[i] > max_expense:
        max_expense = expenses[i]
        most_expensive_category = categories[i]

print("Expense Statistics")
print("==================")
print("Most expensive category:", most_expensive_category)
print("Amount spent:", max_expense)