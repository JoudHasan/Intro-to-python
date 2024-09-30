# Initialize empty lists
recipes_list = []
ingredients_list = []

# Function to take recipe input
def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (separated by commas): ").split(', ')
    
    # Store recipe details in a dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

# Main code
while True:
    try:
        n = int(input("How many recipes would you like to enter? "))
        break
    except ValueError:
        print("Please enter a valid number.")

print(f"Starting to collect {n} recipes.")

# Loop to collect recipes and update ingredients list
for i in range(n):
    recipe = take_recipe()
    print(f"Recipe {i+1} collected.")
    
    # Add unique ingredients to ingredients_list
    for ingredient in recipe['ingredients']:
        if ingredient and ingredient not in ingredients_list:  
            ingredients_list.append(ingredient)
    
    # Append the recipe dictionary to the recipes_list
    recipes_list.append(recipe)

# Determine and display recipe details and difficulty level
for recipe in recipes_list:
    name = recipe['name']
    cooking_time = recipe['cooking_time']
    ingredients = recipe['ingredients']
    num_ingredients = len(ingredients)
    
    # Determine difficulty level based on cooking time and number of ingredients
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    
    # Display recipe details
    print(f"\nRecipe: {name}")
    print(f"Cooking time (minutes): {cooking_time}")
    print(f"Ingredients: {', '.join(ingredients)}")
    print(f"Difficulty: {difficulty}")

# Display all ingredients in alphabetical order
print("\nIngredients you've come across so far:")
for ingredient in sorted(ingredients_list):
    print(ingredient)
