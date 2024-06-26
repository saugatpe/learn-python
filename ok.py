import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order_total = 0  # Initialize the total cost outside the loop

while True:
    try:
        items = input("items: ").title()
        if not items:  # Check for empty input
            continue

        total = items.split(", ")

        for item in total:
            if item in menu:
                price = menu[item]
                order_total += price
                print(f"{item}: ${price:.2f}")
            else:
                print(f"{item}: Not on the menu")

        print(f"Total so far: ${order_total:.2f}")

    except EOFError:
        print(f"Final total: ${order_total:.2f}")
        break  # End the loop on EOFError

# Exit with code 0 explicitly
sys.exit(0)
