score = float(input("Enter Score: "))
try:
    if score <= 1.0:
        if 1.0 >= score >= 0.9:
            print("A")
        elif 0.9 > score >= 0.8:
            print("B")
        elif 0.8 > score >= 0.7:
            print("C")
        elif 0.7 > score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    else:
        raise ValueError()
except ValueError:
    print("Error, number is out of range")
    quit()
