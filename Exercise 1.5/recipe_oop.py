class Recipe:
    all_ingredients = set()  # Class variable to store all unique ingredients

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calculate_difficulty()

    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient)

    def __str__(self):
        return "Recipe: " + self.name + "\n" + \
               "Cooking Time: " + str(self.cooking_time) + " minutes\n" + \
               "Ingredients: " + ", ".join(self.ingredients) + "\n" + \
               "Difficulty: " + self.get_difficulty() + "\n"

    def recipe_search(self, data, search_term):
        print("\nSearching for recipes with '" + search_term + "':")
        found = False
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                found = True
        if not found:
            print("No recipes found with '" + search_term + "'.")

# Main Code to Create and Search Recipes
if __name__ == "__main__":
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)

    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.set_cooking_time(5)

    cake = Recipe("Cake")
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence",
                         "Flour", "Baking Powder", "Milk")
    cake.set_cooking_time(50)

    smoothie = Recipe("Banana Smoothie")
    smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    smoothie.set_cooking_time(5)

    recipes_list = [tea, coffee, cake, smoothie]

    # Display all recipes
    for recipe in recipes_list:
        print(recipe)

    # Search for specific ingredients
    tea.recipe_search(recipes_list, "Water")
    tea.recipe_search(recipes_list, "Sugar")
    tea.recipe_search(recipes_list, "Bananas")
