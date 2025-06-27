inventory = {}

print("Welcome to the Inventory Manager!")

while True:
    print("Choose an option:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Update an item")
    print("4. View inventory")
    print("5. Calculate total value")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        item = input("Enter item name to add: ").strip().lower()
        if item in inventory:
            print("Item already exists. Use option 3 to update it.")
            continue
        try:
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory[item] = (qty, price)
            print(f"{item} added successfully.")
        except ValueError:
            print("Invalid quantity or price. Try again.")

    elif choice == "2":
        item = input("Enter item name to remove: ").strip().lower()
        if item in inventory:
            del inventory[item]
            print(f"{item} removed successfully.")
        else:
            print("Item not found.")

    elif choice == "3":
        item = input("Enter item name to update: ").strip().lower()
        if item in inventory:
            try:
                qty = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                inventory[item] = (qty, price)
                print(f"{item} updated successfully.")
            except ValueError:
                print("Invalid quantity or price. Try again.")
        else:
            print("Item not found.")

    elif choice == "4":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent inventory:")
            for name, (qty, price) in inventory.items():
                print(f"Item: {name}, Quantity: {qty}, Price: ${price}")
    
    elif choice == "5":
        total_value = sum(qty * price for qty, price in inventory.values())
        print(f"\nTotal value of inventory: ${total_value:.2f}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 6.")
