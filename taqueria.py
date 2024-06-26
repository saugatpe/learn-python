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
        item = input("Item: ").title()  # Prompt the user for an item and title case it
        if item in menu:  # Check if the item is in the menu
            price = menu[item]
            order_total += price
            print(f"Total: ${order_total:.2f}")  # Print the running total
        else:
            print(f"{item} is not on the menu.")
    except EOFError:  # Handle the end-of-file (EOF) signal gracefully
        print()  # Print a newline character for neatness
        break  # Exit the loop when EOF is encountered

# Exit with code 0 explicitly (although this is not necessary in most cases)
import sys
sys.exit(0)
