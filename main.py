from print_effects import burn, printer, thunderstorm, wipe, figlet_format
from API import category_search, search
from results_formatter import format_results
from dice_rolls import dice, D20, D100

def main():
    welcome()
    main_menu()
    
    

def welcome():
    burn(figlet_format("DnD CLI Tool!", "starwars"))
    printer('''
    Welcome to the DnD CLI Tool! This tool is designed to help you manage you play Dungeons and Dragons. 
    You can use the command line to look up information about characters, monsters, spells, and more. 
    Enjoy your adventure!''')
    
    
def main_menu(choice=None):
    if not choice:
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
        format_results(result)
    elif choice == '2':
        roll = True
        while roll:
            dice_options = {4: dice, 6: dice, 8: dice, 10: dice, 12: dice, 20: D20, 100: D100}
            faces = int(input("Enter the number of faces on the dice (4, 6, 8, 10, 12, 20, 100): "))
            modifier = int(input("Enter a modifier to add to the roll (enter 0 for no modifier: "))
            d = dice_options[faces](faces, modifier)
            printer(d.roll())
            roll_again = input("Would you like to roll again? (y/n): ")
            if roll_again.lower() != 'y':
                roll = False
        main_menu()
    elif choice == '3':
        printer("Exiting the DnD CLI Tool. Goodbye!")
        exit()
    else:
        printer("Invalid choice. Please try again.")
        main_menu()






if __name__ == "__main__":
    main()
