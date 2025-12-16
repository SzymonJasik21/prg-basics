file_name = 'it_company.csv'
job_title = 'Software Engineer'

count = 1

with open(file_name, 'r') as file:
   for line in file:
      if job_title in line:
         print(f"{count}. {line.strip()}")
         count += 1