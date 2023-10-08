class RecipePlatform:
    # ... (other methods and __init__ remain the same)

    def run(self):
        while True:
            print("\nRecipe Sharing Platform")
            print("1. Add Recipe")
            print("2. Search by Ingredient")
            print("3. Rate a Recipe")
            print("4. Comment on a Recipe")
            print("5. Display All Recipes")
            print("6. Exit")

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    title = input("Enter recipe title: ")
                    ingredients = input("Enter ingredients (comma-separated): ").split(",")
                    instructions = []
                    print("Enter instructions (type 'done' to finish):")
                    while True:
                        instruction = input()
                        if instruction.lower() == 'done':
                            break
                        instructions.append(instruction)
                    author = input("Enter your name: ")
                    recipe = Recipe(title, ingredients, instructions, author)
                    self.add_recipe(recipe)
                    print("Recipe added successfully!")

                elif choice == "2":
                    ingredient = input("Enter an ingredient to search for: ")
                    search_results = self.search_by_ingredient(ingredient)
                    if search_results:
                        print("Search Results:")
                        for i, recipe in enumerate(search_results, 1):
                            print(f"{i}. {recipe.title} by {recipe.author}")
                    else:
                        print("No matching recipes found.")

                elif choice == "3":
                    recipe_number = int(input("Enter the number of the recipe you want to rate: ")) - 1
                    if 0 <= recipe_number < len(self.recipes):
                        recipe = self.recipes[recipe_number]
                        rating = int(input("Enter your rating (1-5): "))
                        self.rate_recipe(recipe, rating)
                        print("Rating added successfully!")
                    else:
                        print("Invalid recipe number.")

                elif choice == "4":
                    recipe_number = int(input("Enter the number of the recipe you want to comment on: ")) - 1
                    if 0 <= recipe_number < len(self.recipes):
                        recipe = self.recipes[recipe_number]
                        comment = input("Enter your comment: ")
                        self.comment_on_recipe(recipe, comment)
                        print("Comment added successfully!")
                    else:
                        print("Invalid recipe number.")

                elif choice == "5":
                    if self.recipes:
                        self.display_all_recipes()
                        recipe_number = int(input("Enter the number of the recipe you want to view: ")) - 1
                        if 0 <= recipe_number < len(self.recipes):
                            recipe = self.recipes[recipe_number]
                            self.display_recipe(recipe)
                        else:
                            print("Invalid recipe number.")
                    else:
                        print("No recipes available.")

                elif choice == "6":
                    print("Exiting Recipe Sharing Platform. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

            except ValueError:
                print("Invalid input. Please enter a valid value.")
            except KeyboardInterrupt:
                print("\nExiting Recipe Sharing Platform. Goodbye!")
                break

rp = RecipePlatform()
rp.run()
