def main():
    purchase = input("How much was the purchase? ")
    percentage = input("What percentage is the GST rate? ")
    gst = calculate_gst(purchase, percentage)
    print(f"GST will be ${gst:.2f}")

def calculate_gst(purchase, percentage):
    price = currency_to_float(purchase)
    percent = percent_to_float(percentage)
    gst = price * percent

    return gst


def currency_to_float(d):
    purchase = input(


def percent_to_float(p):
    # TODO


main()