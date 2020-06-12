from category import Category

class Store:
    def __init__(self, name, categories):
        # pairing the values for this instance and the rest to come
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"Welcome to {self.name}"
        i = 1
        for category in self.categories:
            output += f'\n {i}. {category.name}'
            i += 1
        return output

    def __repr__(self):
        # returns a string
        return f"self.name = {self.name} ; self.categories = {self.categories}"

running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Chicago Cubs Fans Only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "The american kind! lel", [])
soccer_category = Category("Soccer", "The real football! haha", [])

sports_store = Store("Gander Mountain", [running_category, baseball_category, basketball_category, football_category, soccer_category])

choice = -1
# REPL <- Read Evaluate Print Loop!
print(sports_store)
print("type quit to quit!")
while True:
    # READ
    choice = input("Please choose a category (#): ")
    try:    
        # EVALUATE
        if (choice == "quit"):
            break
        choice = int(choice) - 1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
        # PRINT
            print(chosen_category)
        else:
            print("The number you have entered is not a valid option")
    except ValueError:
        print("Please enter a valid option")
