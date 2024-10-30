import mysql.connector

def calculate_difficulty(cooking_time, ingredients):
    """Calculates the difficulty level of the recipe."""
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

def sanitize_ingredients(ingredients):
    """Sanitize ingredients input by splitting and removing extra spaces."""
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
    return ", ".join(ingredients_list)

def create_recipe(conn, cursor):
    """Create a new recipe and add it to the database."""
    name = input("Enter the recipe name: ").strip()
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").strip()

    sanitized_ingredients = sanitize_ingredients(ingredients)
    difficulty = calculate_difficulty(cooking_time, sanitized_ingredients.split(", "))

    insert_query = """
    INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, sanitized_ingredients, cooking_time, difficulty))
    conn.commit()
    print("Recipe added successfully!")

def search_recipe(conn, cursor):
    """Search for recipes by an ingredient."""
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = set()
    for row in results:
        all_ingredients.update(row[0].split(", "))

    print("\nAvailable ingredients:")
    for idx, ingredient in enumerate(sorted(all_ingredients), start=1):
        print(f"{idx}. {ingredient}")

    try:
        choice = int(input("Choose an ingredient by number to search: ")) - 1
        search_ingredient = sorted(all_ingredients)[choice]
    except (ValueError, IndexError):
        print("Invalid choice. Please try again.")
        return

    search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(search_query, ('%' + search_ingredient + '%',))
    results = cursor.fetchall()

    if results:
        print("\nRecipes with the selected ingredient:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Ingredients: {row[2]}, "
                  f"Cooking Time: {row[3]} mins, Difficulty: {row[4]}")
    else:
        print("No recipes found with that ingredient.")

def update_recipe(conn, cursor):
    """Update an existing recipe."""
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("No recipes available to update.")
        return

    print("\nExisting recipes:")
    for row in recipes:
        print(f"ID: {row[0]}, Name: {row[1]}")

    try:
        recipe_id = int(input("Enter the ID of the recipe to update: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if not any(row[0] == recipe_id for row in recipes):
        print(f"No recipe found with ID {recipe_id}.")
        return

    valid_columns = ['name', 'ingredients', 'cooking_time']
    column_to_update = input("Enter the column to update (name, ingredients, cooking_time): ").strip()

    if column_to_update not in valid_columns:
        print(f"Invalid column. Please choose from: {', '.join(valid_columns)}.")
        return

    if column_to_update == 'name':
        new_value = input("Enter the new name: ").strip()
        update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
        cursor.execute(update_query, (new_value, recipe_id))

    elif column_to_update == 'ingredients':
        new_value = input("Enter the new ingredients (comma-separated): ").strip()
        sanitized_ingredients = sanitize_ingredients(new_value)
        update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
        cursor.execute(update_query, (sanitized_ingredients, recipe_id))

    elif column_to_update == 'cooking_time':
        try:
            new_value = int(input("Enter the new cooking time (in minutes): ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
        cursor.execute(update_query, (new_value, recipe_id))

    if column_to_update in ['ingredients', 'cooking_time']:
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        row = cursor.fetchone()
        difficulty = calculate_difficulty(row[0], row[1].split(", "))
        update_query = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
        cursor.execute(update_query, (difficulty, recipe_id))

    conn.commit()
    print("Recipe updated successfully!")

def delete_recipe(conn, cursor):
    """Delete a recipe from the database."""
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("No recipes available to delete.")
        return

    print("\nExisting recipes:")
    for row in recipes:
        print(f"ID: {row[0]}, Name: {row[1]}")

    try:
        recipe_id = int(input("Enter the ID of the recipe to delete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if not any(row[0] == recipe_id for row in recipes):
        print(f"No recipe found with ID {recipe_id}.")
        return

    delete_query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(delete_query, (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

def main_menu(conn, cursor):
    while True:
        print("\nMain Menu:")
        print("1. Add a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    conn = mysql.connector.connect(
        host="localhost",
        user="cf-python",
        password="password",
        database="task_database"
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
    """)

    main_menu(conn, cursor)
