def compute_assessed_value(county, market_value):
    rates = {"Cook": 0.90, "DuPage": 0.80, "McHenry": 0.75, "Kane": 0.60}
    assessment_rate = rates.get(county, 0.70)
    return market_value * assessment_rate

total_market_value = 0
total_assessed_value = 0

response = input("Do you want to enter home data? (Yes/No): ").strip().lower()
while response == "yes":
    county = input("Enter county: ").strip().title()
    market_value = float(input("Enter market value of the home: "))

    assessed_value = compute_assessed_value(county, market_value)
    total_market_value += market_value
    total_assessed_value += assessed_value

    print(f"County: {county}, Assessed Value: ${assessed_value:.2f}")

    response = input("Do you want to enter another home? (Yes/No): ").strip().lower()

print(f"\nTotal Market Value: ${total_market_value:.2f}")
print(f"Total Assessed Value: ${total_assessed_value:.2f}")
