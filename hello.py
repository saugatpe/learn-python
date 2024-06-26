    while True:
        try:
            items = input("items: ").title()

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

            total = items.split(", ")
            print(items)

            order_total = 0
            # Initialize the total cost

            for item in total:
                if item in menu:
                    price = menu[item]
                    order_total = price + order_total
                    print(f"{item}: ${price:.2f}")
                else:
                    print(f"{item}: Not on the menu")

            print(f"Total: ${order_total:.2f}")

        except EOFError:
            break  # End the loop on EOFError
