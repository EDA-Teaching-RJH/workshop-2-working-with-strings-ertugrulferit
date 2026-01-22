def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    input_without_symbol = d.replace("£", " ")
    return float(input_without_symbol)

def percent_to_float(p):
    input_without_percent = p.replace("%", " ")
    return float(input_without_percent) / 100

main()
