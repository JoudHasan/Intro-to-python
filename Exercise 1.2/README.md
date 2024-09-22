# Recipe App Data Structures

## Overview

In this task, I created a basic data structure to store and manage recipes for a simple Recipe app. Each recipe contains essential information such as the recipe's name, cooking time, and ingredients. Additionally, all recipes are stored in an outer structure that can be easily extended as new recipes are added. Below, I explain the reasoning behind my choice of data structures and the steps I followed to implement the solution.

## Data Structures Used

### 1. **Dictionary for Each Recipe**

Each recipe is stored as a **dictionary**. A dictionary was chosen for the following reasons:

- **Key-value pairs**: A dictionary is ideal for storing recipe attributes where each key refers to a specific attribute (e.g., recipe name, cooking time, and ingredients).
- **Readability**: Dictionaries provide a clear and intuitive way to store the attributes of each recipe. For instance, `"name"` maps to the recipe's name, and `"ingredients"` maps to a list of ingredients.
- **Flexibility**: Dictionaries allow easy modification of values associated with each key, making it simple to update or extend recipes as needed.

#### Example Structure for `recipe_1`:

```python
recipe_1 = {
    'name': 'Tea',
    'cooking_time': 5,  # Cooking time in minutes
    'ingredients': ['Tea leaves', 'Sugar', 'Water']
}

### In this example:

1. The name is a string that holds the name of the recipe ("Tea").
2. The cooking_time is an integer representing the cooking time in minutes (5).
3. The ingredients is a list of strings representing the ingredients needed for the recipe (['Tea leaves', 'Sugar', 'Water']).

2. ### List for Storing Multiple Recipes (all_recipes)
To store all recipes, I chose a list. A list was chosen because:

. Sequential nature: Lists maintain the order in which recipes are added, which is useful for displaying recipes in the order they were created.
. Scalability: A list is flexible and allows adding, removing, and modifying recipes as needed. As new recipes are created, they can easily be appended to the list.
. Ease of iteration: Lists make it easy to iterate over the recipes, for example, when printing the ingredients for each recipe.

### Example Structure for all_recipes:
all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

This list contains multiple dictionaries, each representing a different recipe.

### Steps Implemented

1. Created a dictionary for recipe_1:

Name: "Tea"
Cooking time: 5 minutes
Ingredients: ['Tea leaves', 'Sugar', 'Water']

2. Created an outer list called all_recipes:
This list stores multiple recipe dictionaries, making it easy to manage and access different recipes.

3. Generated four additional recipes (recipe_2 to recipe_5):
Each recipe has its own unique name, cooking time, and ingredients.

4. Added all recipes to all_recipes:
Used the append() method to add each recipe to the list sequentially.

5. Printed the ingredients for each recipe:
Iterated over the all_recipes list to display the ingredients of each recipe.

### Example Code
# Creating individual recipes
recipe_1 = {
    'name': 'Tea',
    'cooking_time': 5,
    'ingredients': ['Tea leaves', 'Sugar', 'Water']
}

recipe_2 = {
    'name': 'Pancakes',
    'cooking_time': 15,
    'ingredients': ['Flour', 'Eggs', 'Milk', 'Butter', 'Sugar']
}

recipe_3 = {
    'name': 'Omelette',
    'cooking_time': 10,
    'ingredients': ['Eggs', 'Salt', 'Pepper', 'Butter']
}

recipe_4 = {
    'name': 'Salad',
    'cooking_time': 5,
    'ingredients': ['Lettuce', 'Tomatoes', 'Cucumber', 'Olive oil']
}

recipe_5 = {
    'name': 'Sandwich',
    'cooking_time': 7,
    'ingredients': ['Bread', 'Lettuce', 'Tomatoes', 'Cheese', 'Ham']
}

# Adding recipes to a list
all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

# Printing the ingredients for each recipe
for recipe in all_recipes:
    print(f"Ingredients for {recipe['name']}: {recipe['ingredients']}")


#### Why I Chose These Data Structures

1. Dictionaries were chosen for individual recipes because they allow easy access to recipe attributes through keys. The flexibility of dictionaries makes it easy to add or modify information about each recipe, such as adding more ingredients or changing the cooking time.

2. Lists were chosen for all_recipes because they provide an ordered sequence of recipes, allowing for easy expansion and iteration. This structure is scalable and supports future modifications, such as adding more recipes or removing existing ones.
```
