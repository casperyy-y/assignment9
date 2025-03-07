def compute_square_footage(length, width, height):
    return 2 * (length * width + length * height + width * height)

response = input("Do you want to enter room dimensions? (Yes/No): ").strip().lower()
while response == "yes":
    length = float(input("Enter room length (ft): "))
    width = float(input("Enter room width (ft): "))
    height = float(input("Enter room height (ft): "))

    square_footage = compute_square_footage(length, width, height)
    gallons_needed = square_footage / 50

    print(f"Room Square Footage: {square_footage:.2f} sq ft")
    print(f"Gallons of Paint Needed: {gallons_needed:.2f}")

    response = input("Do you want to enter another room? (Yes/No): ").strip().lower()
