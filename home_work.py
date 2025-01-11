
menu = {
    "Burger": 5.99,
    "Pizza": 7.99,
    "Pasta": 6.49,
    "Salad": 4.49,
    "Soda": 1.99
}


# Function to display the menu
def display_menu():
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: {price:.2f}EUR")


# Function to take the customer's order
def take_order():
    order = []  # List to store the items ordered
    while True:
        item = input("\nCfare deshironi te porosisni? (shtypni 'asgje'per ta mbyllur): ").title()

        # If the user types 'done', stop the ordering process
        if item.lower() == 'asgje':
            break

        # If the item is in the menu, add it to the order
        elif item in menu:
            order.append(item)
            print(f"{item} u shtua ne cante.")
        else:
            print("Na vjen keq nuk e kemi kete produkt, Ju lutem zgjidhni nga menuja.")

    return order


# Function to calculate the total price of the order
def calculate_total(order):
    total = 0
    for item in order:
        total += menu[item]  # Add the price of each ordered item
    return total


# Function to display the receipt
def show_receipt(order, total):
    print("\nYour Order:")
    for item in order:
        print(f"- {item}")
    print(f"\nTotal: ${total:.2f}")
    print("Faleminderit qe na zgjodhet ne!")


# Main program
print("Welcome to the Restaurant!")

# Display the menu to the user
display_menu()

# Take the customer's order
order = take_order()

# Calculate the total of the order
total = calculate_total(order)

# Show the receipt
show_receipt(order, total)




