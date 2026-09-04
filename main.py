from print_effects import burn, printer, thunderstorm, wipe, figlet_format
from API import category_search, search

def main():
    welcome()
    

def welcome():
    burn(figlet_format("DnD CLI Tool!", "starwars"))
    printer('''
    Welcome to the DnD CLI Tool! This tool is designed to help you manage you play Dungeons and Dragons. 
    You can use the command line to look up information about characters, monsters, spells, and more. 
    Enjoy your adventure!''')
    main_menu()

def main_menu():
    printer('''
                    Main Menu:
    1. Search Open5e    2. Roll Dice   3. Exit
    ''')
    choice = input("Please select an option (1-4): ")
    if choice == '1':
        number = 0
        options = search()
        for key in options.data.keys():
            number += 1
            printer(f"{number}: {key} at URL: {options.data[key]}.")
        selction = int(input("Enter the number you would like to query: "))
        #selected_key = list(options.data.keys())[selction-1]
        #category = category_search(selected_key)
        #print(category.url)
        #printer(f"There are {monsters.data['count']} creatures in the Open5e database. Search for a specific creature by name.")
        #query = input("Creature name: ")
        #result = monsters.search_page(query)
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
