import mysql.connector

def create_connection():
    """Establish a connection to the MySQL server."""
    conn = mysql.connector.connect(
        host="localhost",
        user="cf-python",
        password="password"
    )
    return conn

def create_database(cursor):
    """Create the task_database if it does not exist."""
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database;")
    cursor.execute("USE task_database;")

def initialize_table(cursor):
    """Create the Recipes table if it does not exist in task_database."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    );
    """)

def calculate_difficulty(cooking_time, ingredients):
    """Calculate the difficulty level of the recipe."""
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

def display_and_select_recipe(cursor):
    """Display all recipes and prompt the user to select one by ID."""
    cursor.execute("SELECT id, name FROM Recipes;")
    recipes = cursor.fetchall()
    if not recipes:
        print("No recipes available.")
        return None

    print("\nExisting recipes:")
    for row in recipes:
        print(f"ID: {row[0]}, Name: {row[1]}")
    
    try:
        recipe_id = int(input("Enter the ID of the recipe to select: ").strip())
        if not any(row[0] == recipe_id for row in recipes):
            print(f"No recipe found with ID {recipe_id}.")
            return None
        return recipe_id
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def update_difficulty(cursor, recipe_id):
    """Recalculate and update the difficulty of a recipe based on current cooking time and ingredients."""
    cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s;", (recipe_id,))
    row = cursor.fetchone()
    if row:
        difficulty = calculate_difficulty(row[0], row[1].split(", "))
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s;", (difficulty, recipe_id))

def create_recipe(conn, cursor):
    """Create a new recipe and add it to the database."""
    name = input("Enter the recipe name: ").strip()
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").strip()

    sanitized_ingredients = sanitize_ingredients(ingredients)
    difficulty = calculate_difficulty(cooking_time, sanitized_ingredients.split(", "))

    insert_query = """
    INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, (name, sanitized_ingredients, cooking_time, difficulty))
    conn.commit()
    print("Recipe added successfully!")

def search_recipe(cursor):
    """Search for recipes by an ingredient with enhanced formatting."""
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes;")
    results = cursor.fetchall()

    all_ingredients = set()
    for row in results:
        all_ingredients.update(row[0].split(", "))

    print("\nAvailable ingredients:")
    for idx, ingredient in enumerate(sorted(all_ingredients), start=1):
        print(f"{idx}. {ingredient}")

    try:
        choice = int(input("Choose an ingredient by number to search: ").strip()) - 1
        search_ingredient = sorted(all_ingredients)[choice]
    except (ValueError, IndexError):
        print("Invalid choice. Please try again.")
        return

    search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s;"
    cursor.execute(search_query, ('%' + search_ingredient + '%',))
    results = cursor.fetchall()

    if results:
        print("\nRecipes with the selected ingredient:")
        for row in results:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Ingredients:")
            for ingredient in row[2].split(", "):
                print(f"  - {ingredient}")
            print(f"Cooking Time: {row[3]} mins")
            print(f"Difficulty: {row[4]}")
            print("\n" + "-" * 30 + "\n")
    else:
        print("No recipes found with that ingredient.")

def update_recipe(conn, cursor):
    """Update an existing recipe."""
    recipe_id = display_and_select_recipe(cursor)
    if recipe_id is None:
        return

    cursor.execute("SELECT * FROM Recipes WHERE id = %s;", (recipe_id,))
    row = cursor.fetchone()
    print("\nCurrent Recipe Details:")
    print(f"Name: {row[1]}, Ingredients: {row[2]}, Cooking Time: {row[3]}, Difficulty: {row[4]}")

    valid_columns = ['name', 'ingredients', 'cooking_time']
    column_to_update = input("Enter the column to update (name, ingredients, cooking_time): ").strip()

    if column_to_update not in valid_columns:
        print(f"Invalid column. Please choose from: {', '.join(valid_columns)}.")
        return

    if column_to_update == 'name':
        new_value = input("Enter the new name: ").strip()
    elif column_to_update == 'ingredients':
        new_value = sanitize_ingredients(input("Enter the new ingredients (comma-separated): ").strip())
    elif column_to_update == 'cooking_time':
        try:
            new_value = int(input("Enter the new cooking time (in minutes): ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    update_query = f"UPDATE Recipes SET {column_to_update} = %s WHERE id = %s;"
    cursor.execute(update_query, (new_value, recipe_id))

    if column_to_update in ['ingredients', 'cooking_time']:
        update_difficulty(cursor, recipe_id)

    conn.commit()
    print("Recipe updated successfully!")

def delete_recipe(conn, cursor):
    """Delete a recipe from the database."""
    recipe_id = display_and_select_recipe(cursor)
    if recipe_id is None:
        return

    cursor.execute("DELETE FROM Recipes WHERE id = %s;", (recipe_id,))
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
            search_recipe(cursor)
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
    conn = create_connection()
    cursor = conn.cursor()

    create_database(cursor)
    initialize_table(cursor)

    main_menu(conn, cursor)
   