def company_data():
    company = "ABC Data"
    phone = "555-123-009"
    employees = 25
    remote_work = True
    big_company = employees > 100
    income = 4500000
    income_per_person = income / employees
    return company, phone, employees, remote_work, big_company, income, income_per_person

if __name__ == "__main__":
    print(company_data())