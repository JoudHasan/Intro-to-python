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
    # Adds number to each element in the list
    numbered_list = list(enumerate(data["all_ingredients"], 1))  # Use correct key with quotes
    print("Ingredients List:")

    for count, ele in numbered_list:
        print(count, ele)

    try:
        num = int(input("Enter the number for ingredients you would like to search: ")) - 1  # Adjust for 0-based indexing
        ingredient_searched = numbered_list[num][1]  # Access the correct element

        print("Searching for recipes with", ingredient_searched, "...")

    except ValueError:
        print("Only numbers are allowed.")
    except IndexError:  # Use IndexError since we're accessing a list
        print("The number you selected does not exist.")
    except KeyboardInterrupt:
        print("\nSearch interrupted by the user.")
    else:
        for ele in data["recipes_list"]:
            if ingredient_searched in ele["ingredients"]:
                display_recipe(ele)

# Load data from a pickle file
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
