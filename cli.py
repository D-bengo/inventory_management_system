import requests

BASE_URL = "http://127.0.0.1:5000"

while True:

    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. View Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Search OpenFoodFacts")
    print("7. Exit")

    choice = input("Choose option: ")

    # View inventory
    if choice == "1":

        response = requests.get(f"{BASE_URL}/inventory")

        print(response.json())

    # View item
    elif choice == "2":

        item_id = input("Enter item ID: ")

        response = requests.get(
            f"{BASE_URL}/inventory/{item_id}"
        )

        print(response.json())

    # Add item
    elif choice == "3":

        data = {
            "barcode": input("Barcode: "),
            "product_name": input("Product Name: "),
            "brand": input("Brand: "),
            "price": float(input("Price: ")),
            "stock": int(input("Stock: "))
        }

        response = requests.post(
            f"{BASE_URL}/inventory",
            json=data
        )

        print(response.json())

    # Update item
    elif choice == "4":

        item_id = input("Enter item ID: ")

        data = {
            "price": float(input("New Price: ")),
            "stock": int(input("New Stock: "))
        }

        response = requests.patch(
            f"{BASE_URL}/inventory/{item_id}",
            json=data
        )

        print(response.json())

    # Delete item
    elif choice == "5":

        item_id = input("Enter item ID: ")

        response = requests.delete(
            f"{BASE_URL}/inventory/{item_id}"
        )

        print(response.json())

    # Search API
    elif choice == "6":

        barcode = input("Enter barcode: ")

        response = requests.get(
            f"{BASE_URL}/search?barcode={barcode}"
        )

        print(response.json())

    elif choice == "7":
        break

    else:
        print("Invalid choice")