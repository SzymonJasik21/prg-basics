###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r", encoding="utf-8") as file:
   email = file.read()
#email = ... (email content)


# regular expression pattern
# for amounts
pattern = r'\d+\.?\d*'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total_value = 0
for amount in amounts:
   total_value += float(amount)

# print result
print(f"Total money spent: {total_value:.2f}")