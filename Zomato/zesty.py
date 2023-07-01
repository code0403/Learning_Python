import json
from tabulate import tabulate


menu = []  # List to store menu items
orders = {}  # Dictionary to store orders
order_id_counter = 1

def display_menu():
    print("Menu Items:")
    if len(menu) == 0:
        print("No items in the menu.")
    else:
        table = []
        for item in menu:
            table.append([item['dish_id'], item['dish_name'], item['price'], 'Available' if item['availability'] else 'Not Available'])
        print(tabulate(table, headers=["Dish ID:", "Dish Name:", "Price:", "Availability:"], tablefmt="grid"))
        print()

def add_menu_item():
    dish_id = int(input("Enter the ID of the dish: "))
    dish_name = input("Enter the name of the snack: ")
    dish_price = float(input("Enter the price of the dish: ₹ "))
    availability = input("Is the dish available? (yes/no): ").lower()

    if availability == "yes":
        availability = True
    else:
        availability = False

    menu.append({
        "dish_id": dish_id,
        "dish_name": dish_name,
        "price": dish_price,
        "availability": availability
    })
    print(f"Menu item added successfully: {dish_name}")

def remove_menu_item():
    dish_id = int(input("Enter the dish ID of the item to be removed: "))

    for item in menu:
        if item["dish_id"] == dish_id:
            menu.remove(item)
            print("Menu item removed successfully.")
            return

    print("Menu item not found.")

def update_menu_item_availability():
    dish_id = int(input("Enter the dish ID of the item to update availability: "))

    for item in menu:
        if item["dish_id"] == dish_id:
            availability = input("Is the dish available? (yes/no): ").lower()

            if availability == "yes":
                item["availability"] = True
                print("Menu item availability updated successfully.")
            elif availability == "no":
                item["availability"] = False
                print("Menu item availability updated successfully.")
            else:
                print("Invalid choice.")
            return

    print("Menu item not found.")

def take_order():
    global order_id_counter
    customer_name = input("Enter customer name: ")

    order_items = []
    while True:
        dish_id = input("Enter dish ID (Enter 'done' to finish): ")
        if dish_id == "done":
            break

        dish = None
        for item in menu:
            if item["dish_id"] == int(dish_id):
                dish = item
                break

        if dish:
            if dish["availability"]:
                order_items.append(dish)
                print("Dish added to order.")
            else:
                print("Dish is not available.")
        else:
            print("Dish not found.")

    if order_items:
        order_id = order_id_counter
        order_id_counter += 1
        total_price = sum(item["price"] for item in order_items)
        orders[order_id] = {
            "customer_name": customer_name,
            "order_items": order_items,
            "status": "received",
            "total_price": total_price
        }
        print("Order placed successfully.")
        print(f"Order ID: {order_id}")
        print(f"Total Price: ₹ {total_price}")
    else:
        print("No dishes added to the order.")

def update_order_status():
    order_id = int(input("Enter order ID: "))
    if order_id in orders:
        status = input("Enter new order status (recevied, delivered, pending): ")
        orders[order_id]["status"] = status
        print("Order status updated successfully.")
    else:
        print("Order not found.")

def review_orders():
    if not orders:
        print("No orders to review.")
        return

    print("Orders:")
    print("1. Review all orders")
    print("2. Filter orders by status")
    choice = input("Enter your choice: ")

    if choice == "1":
        for order_id, order in orders.items():
            print(f"Order ID: {order_id}")
            print(f"Customer Name: {order['customer_name']}")
            print("Order Items:")
            for item in order["order_items"]:
                print(f"Dish ID: {item['dish_id']}")
                print(f"Dish Name: {item['dish_name']}")
                print(f"Price: {item['price']}")
            print(f"Status: {order['status']}")
            print(f"Total Price: ₹ {order['total_price']}")
            print()
    elif choice == "2":
        status_filter = input("Enter the status to filter orders: ")
        filtered_orders = filter(lambda order: order[1]['status'] == status_filter, orders.items())
        for order_id, order in filtered_orders:
            print(f"Order ID: {order_id}")
            print(f"Customer Name: {order['customer_name']}")
            print("Order Items:")
            for item in order["order_items"]:
                print(f"Dish ID: {item['dish_id']}")
                print(f"Dish Name: {item['dish_name']}")
                print(f"Price: {item['price']}")
            print(f"Status: {order['status']}")
            print(f"Total Price: ₹ {order['total_price']}")
            print()
    else:
        print("Invalid choice.")

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            global menu, orders, order_id_counter
            menu = data["menu"]
            orders = data["orders"]
            order_id_counter = data["order_id_counter"]
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Starting with an empty menu and orders.")

def save_data():
    data = {
        "menu": menu,
        "orders": orders,
        "order_id_counter": order_id_counter
    }
    with open("data.json", "w") as file:
        json.dump(data, file)
        print("Data saved successfully.")

def main():
    load_data()


    print("Zomato Chronicles: The Great Food Fiasco")
    while True:
        print("Welcome to Zesty Zomato!")
        print("1. Display Menu")
        print("2. Add Menu Item")
        print("3. Remove Menu Item")
        print("4. Update Menu Item Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            remove_menu_item()
        elif choice == "4":
            update_menu_item_availability()
        elif choice == "5":
            take_order()
        elif choice == "6":
            update_order_status()
        elif choice == "7":
            review_orders()
        elif choice == "8":
            save_data()
            print("Thank you for using Zesty Zomato. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
