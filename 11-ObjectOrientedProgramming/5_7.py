from statistics_tool import Statistics

stats = Statistics()

data = [12, 37, 6, 9, 17]
for value in data:
    stats.add_value(value)

stats.display_numbers()
stats.print_results()