from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "mysql+mysqlconnector://cf-python:Password@localhost/task_database"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Base class
Base = declarative_base()

# Recipe Model
class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"

    def __str__(self):
        return (f"Recipe ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Ingredients: {self.ingredients}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.difficulty}\n" + "-"*20)

    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()
        if self.cooking_time < 10 and len(ingredients_list) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 20 and len(ingredients_list) < 6:
            self.difficulty = "Medium"
        elif self.cooking_time >= 20 and len(ingredients_list) < 6:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# Create the table in the database
Base.metadata.create_all(engine)

# Function to create a new recipe
def create_recipe():
    name = input("Enter the recipe name: ")
    if len(name) > 50:
        print("Name too long! Limit to 50 characters.")
        return

    try:
        cooking_time = int(input("Enter the cooking time in minutes: "))
    except ValueError:
        print("Invalid cooking time. Please enter a number.")
        return

    ingredients = []
    num_ingredients = int(input("How many ingredients? "))
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)

    ingredients_str = ", ".join(ingredients)
    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time)
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()
    print("Recipe created successfully!")

# Function to view all recipes
def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return
    for recipe in recipes:
        print(recipe)

# Function to search recipes by ingredients
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for row in results:
        ingredients_list = row[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i + 1}. {ingredient}")

    print("Enter the numbers corresponding to ingredients separated by spaces (e.g., '3 5 7'):")
    selected_indices = input("Your choice: ")

    try:
        selected_indices = list(map(int, selected_indices.split()))
        if any(num < 1 or num > len(all_ingredients) for num in selected_indices):
            print("One or more selected numbers are out of range. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        return

    search_ingredients = [all_ingredients[i - 1] for i in selected_indices]
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]

    recipes = session.query(Recipe).filter(*conditions).all()
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print("No recipes found with the selected ingredients.")

# Function to edit a recipe
def edit_recipe():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    for recipe in recipes:
        print(f"{recipe.id}: {recipe.name}")
    try:
        recipe_id = int(input("Enter recipe ID to edit: "))
        recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).one_or_none()
        if not recipe_to_edit:
            print("Recipe not found.")
            return
    except ValueError:
        print("Invalid ID.")
        return

    print("1. Name\n2. Ingredients\n3. Cooking Time")
    try:
        choice = int(input("Choose field to edit: "))
        if choice == 1:
            recipe_to_edit.name = input("New name: ")
        elif choice == 2:
            ingredients = input("New ingredients (comma separated): ")
            recipe_to_edit.ingredients = ingredients
        elif choice == 3:
            recipe_to_edit.cooking_time = int(input("New cooking time: "))
        else:
            print("Invalid choice.")
            return
        recipe_to_edit.calculate_difficulty()
        session.commit()
        print("Recipe updated successfully!")
    except ValueError:
        print("Invalid input.")

# Function to delete a recipe
def delete_recipe():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    for recipe in recipes:
        print(f"{recipe.id}: {recipe.name}")
    try:
        recipe_id = int(input("Enter recipe ID to delete: "))
        recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).one_or_none()
        if not recipe_to_delete:
            print("Recipe not found.")
            return

        confirm = input("Are you sure you want to delete this recipe? (yes/no): ")
        if confirm.lower() == 'yes':
            session.delete(recipe_to_delete)
            session.commit()
            print("Recipe deleted successfully!")
    except ValueError:
        print("Invalid ID.")

# Main menu function
def main_menu():
    while True:
        print("\n--- Recipe App ---")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit")

        choice = input("Choose an option: ")
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice.lower() == 'quit':
            session.close()
            engine.dispose()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()
