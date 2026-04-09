
# 1. CREATE A SMALL PROGRAM TO MANAGE PRODUCTS.
# THE PROGRAM SHOULD ADD, VIEW, SEARCH, UNDATE AND DELETE PRODUCTS

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    # ADD A METHOD TO SHOW PRODUCT INFO
    def __str__(self):
        return f"""
        =================================
            MINI INVENTORY SYSTEM
        =================================
        Id: {self.product_id}
        Name: {self.name}
        Price: {self.price}
        Quantity: {self.quantity}
        ===================================
"""

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product Added Successfully")

    # ADD A METHOD TO SHOW ALL PRODUCTS

    def view_products(self):
        if len(self.products) == 0: # If the list if empty
            print("Inventory is empty") # Show this message
        else:
            for product in self.products:
                print(product) # Call the method fron the product class
                print("-" * 20) #

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

def show_menu():
        print("\n=== INVENTORY MENU===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Exit")

inventory = Inventory()

while True:

    show_menu()
    option = input("Enter your option: ")

    if option == "1":
        product_id = (input("Enter product id: "))
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        product = Product(product_id, name, price, quantity)
        inventory.add_product(product)

    elif option == "2":
        inventory.view_products()

    elif option == "3":
        search_id = (input("Enter product id:"))
        found = inventory.search_product(search_id)

        if found:
            print("Product found")
        else:
            print("Product not found")

    elif option == "4":
        print("Goodbye")
        break #

    else:
        print("Invalid option. Try again")
