from print_effects import burn, printer, thunderstorm, wipe, figlet_format
from API import category_search, search

def main():
    welcome()
    main_menu()
    
    

def welcome():
    burn(figlet_format("DnD CLI Tool!", "starwars"))
    printer('''
    Welcome to the DnD CLI Tool! This tool is designed to help you manage you play Dungeons and Dragons. 
    You can use the command line to look up information about characters, monsters, spells, and more. 
    Enjoy your adventure!''')
    
def main_menu():
    printer('''
                    Main Menu:
    1. Search Open5e    2. Roll Dice   3. Exit
    ''')
    choice = input("Please select an option (1-4): ")
    if choice == '1':
        avoid = ["services", "rules", "rulesets", "subclasses", "images", "environments", "itemrarities", "alignments", "creaturesets", "creaturetypes", "gamesystems", "publishers", "licenses", "documents", "itemcategories", "itemsets", "weaponproperties"]
        number = 0
        options = search()
        keys = list(options.data.keys())
        for key in keys:
            if key in avoid:
                options.data.pop(key)
        for key in options.data.keys():
            number += 1
            print(f"{number}: {key} at URL: {options.data[key]}.")
        selection = int(input("Enter the number you would like to query: "))
        selected_key = list(options.data.keys())[selection-1]
        category = category_search(selected_key)
        printer(f"There are {category.data['count']} {selected_key} in the Open5e database. Search for a specific {selected_key} by name.")
        query = input("Query name: ")
        result = category.search_page(query)
        print(result)
    elif choice == '2':
        pass
    elif choice == '3':
        printer("Exiting the DnD CLI Tool. Goodbye!")
        exit()
    else:
        printer("Invalid choice. Please try again.")
        main_menu()






if __name__ == "__main__":
    main()
