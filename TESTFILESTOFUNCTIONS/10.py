def computepay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * (rate * 1.5)
        pay = regular_pay + overtime_pay
    else:
        pay = hours * rate
    return pay

if __name__ == "__main__":
    print(computepay(45, 10))
    print(computepay(40, 10))
    print(computepay(30, 15))