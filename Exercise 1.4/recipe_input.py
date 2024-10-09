import pickle

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    return difficulty

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (separated by commas): ").split(',')
    
    ingredients = [ingredient.strip() for ingredient in ingredients]  # Clean up spaces
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    
    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

# Get the filename for saving/loading recipes
filename = input("Enter the filename for your recipes: ")

# Try to load the existing data from the file
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File {filename} not found. Initializing new recipe data.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
else:
    print(f"File {filename} loaded successfully.")
finally:
    recipes_list = data.get('recipes_list', [])
    all_ingredients = data.get('all_ingredients', [])

# Ask the user how many recipes to enter
num_recipes = int(input("How many recipes would you like to enter? "))

# Add the recipes
for i in range(0, num_recipes):
    recipe = take_recipe()

    # Add new ingredients to all_ingredients if not already present
    for element in recipe["ingredients"]:
        if element not in all_ingredients:
            all_ingredients.append(element)
    
    # Add the new recipe to the recipes_list
    recipes_list.append(recipe)
    print("Recipe added successfully!")

# Update the dictionary with the new data
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

# Save the updated data to the binary file
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Recipes successfully saved to {filename}!")
