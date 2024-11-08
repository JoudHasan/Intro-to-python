class ShoppingList:
    def __init__(self, list_name):
        # Initialize the shopping list with a name and an empty list
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        # Add item to the shopping list if it's not already present
        if item not in self.shopping_list:
            self.shopping_list.append(item)
        else:
            print(item + " is already in the shopping list.")

    def remove_item(self, item):
        # Remove item from the shopping list if it exists
        if item in self.shopping_list:
            self.shopping_list.remove(item)
        else:
            print(item + " is not in the shopping list.")

    def view_list(self):
        # Display the contents of the shopping list
        if self.shopping_list:
            print("Shopping list '" + self.list_name + "':")
            for item in self.shopping_list:
                print("- " + item)
        else:
            print("The shopping list '" + self.list_name + "' is empty.")


# Create an instance of ShoppingList called pet_store_list
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add items to the list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove an item from the list
pet_store_list.remove_item("flea collars")

# Try to add a duplicate item
pet_store_list.add_item("frisbee")

# Display the shopping list
pet_store_list.view_list()
