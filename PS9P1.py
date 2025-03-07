def compute_forecast(month, sales):
    forecast_rates = {
        "Jan": 0.10, "Feb": 0.10, "Mar": 0.10,
        "Apr": 0.15, "May": 0.15, "Jun": 0.15,
        "Jul": 0.20, "Aug": 0.20, "Sep": 0.20,
        "Oct": 0.25, "Nov": 0.25, "Dec": 0.25
    }
    forecast_percent = forecast_rates.get(month, 0)
    return sales * (1 + forecast_percent)

response = input("Do you want to enter sales data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month: ").strip().title()
    sales = float(input("Enter sales amount: "))

    next_month_sales = compute_forecast(month, sales)
    print(f"Last Name: {last_name}, Next Month's Forecasted Sales: ${next_month_sales:.2f}")

    response = input("Do you want to enter another sales record? (Yes/No): ").strip().lower()
