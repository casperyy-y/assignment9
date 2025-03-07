def compute_ticket_price(miles):
    if miles >= 30:
        return 12
    elif 20 <= miles < 30:
        return 10
    elif 10 <= miles < 20:
        return 8
    else:
        return 5

total_revenue = 0

response = input("Do you want to enter ticket data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter passenger last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))

    price = compute_ticket_price(miles)
    total_revenue += price

    print(f"Passenger: {last_name}, Ticket Price: ${price:.2f}")

    response = input("Do you want to enter another ticket? (Yes/No): ").strip().lower()

print(f"\nTotal Revenue from Tickets: ${total_revenue:.2f}")
