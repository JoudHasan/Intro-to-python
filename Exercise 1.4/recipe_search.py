import pickle

# function to display the recipe
def display_recipe(recipe):
    print("")
    print("Recipe: ", recipe["name"])
    print("Cooking Time (mins): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ele in recipe["ingredients"]:
        print("- ", ele)
    print("Difficulty: ", recipe["difficulty"])
    print("")


# function to search ingredients
def search_ingredients(data):
    # adds number to each element in the list
    available_ingredients = enumerate(data["all_ingredients"])
    # put enumerated data into a list
    numbered_list = list(available_ingredients)
    print("Ingredients List: ")

    for ele in numbered_list:
        print(ele[0], ele[1])
    try:
        num = int(input("Enter the number for ingredients you would like to search: "))
        ingredient_searched = numbered_list[num][1]
        print("Searching for recipes with", ingredient_searched, "...")
    except ValueError:
        print("Only numbers are allowed")
    except:
        print(
            "Oops! Your input doesn't match any ingredients. Make sure you enter a number that matches the ingredients list."
        )
    else:
        for ele in data["recipes_list"]:
            if ingredient_searched in ele["ingredients"]:
                display_recipe(ele)


filename = input("Enter the name of the file you want to save to: ") + '.bin'

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
        print("File loaded successfully!")
except FileNotFoundError:
    print("No files match that name - please try again")
except Exception as e:
    print(f"Oops, there was an unexpected error: {e}")
else:
    search_ingredients(data)
