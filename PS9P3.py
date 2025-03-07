def compute_price(msrp, make, model, ev_code):
    discount_rates = {
        "Honda Accord": 0.10,
        "Toyota Rav4": 0.15,
    }
    if ev_code.upper() == "Y":
        discount = 0.30
    else:
        discount = discount_rates.get(f"{make} {model}", 0.05)

    discounted_price = msrp * (1 - discount)
    total_price = discounted_price * 1.07  # Add 7% sales tax
    return total_price

total_msrp = 0
total_sales_price = 0

response = input("Do you want to enter car data? (Yes/No): ").strip().lower()
while response == "yes":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    ev_code = input("Is this an electric vehicle? (Y/N): ").strip().upper()
    msrp = float(input("Enter MSRP: "))

    total_price = compute_price(msrp, make, model, ev_code)
    total_msrp += msrp
    total_sales_price += total_price

    print(f"Car Make: {make}, Model: {model}, Final Price: ${total_price:.2f}")

    response = input("Do you want to enter another car? (Yes/No): ").strip().lower()

print(f"\nTotal MSRP: ${total_msrp:.2f}")
print(f"Total Sales Price (after tax & discount): ${total_sales_price:.2f}")
