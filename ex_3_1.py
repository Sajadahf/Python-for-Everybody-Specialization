
hours = int(input("Enter hours: "))
rate_per_hrs = float(input("Enter rate_per_hrs: "))
if hours <= 40:
    pay = hours * rate_per_hrs
    print(pay)
else:
    pay = (40 * rate_per_hrs) + ((hours - 40) * (rate_per_hrs * 1.5))
    print(pay)
