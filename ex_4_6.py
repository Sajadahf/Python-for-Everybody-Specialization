def main():
    hours = float(input("Enter hours: "))
    rate_per_hours = float(input("Enter rate: "))
    pay = computepay(hours, rate_per_hours)
    print("Pay", pay)

def computepay(h, r):
    if h <= 40:
        pay = h * r
        return pay

    else:
        pay = (40.0 * r) + (((h - 40.0) * 1.5) * r)
        return pay

main()
