from print_effects import burn, printer, thunderstorm, wipe, figlet_format
from API import category_search

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
    1. Search Creatures    2. Search Spells    3. Roll Dice    4. Exit
    ''')
    choice = input("Please select an option (1-4): ")
    if choice == '1':
        monsters = category_search("creatures")
        printer(f"There are {monsters.data['count']} creatures in the Open5e database. Search for a specific creature by name.")
        query = input("Creature name: ")
        result = monsters.search_page(query)
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        printer("Exiting the DnD CLI Tool. Goodbye!")
        exit()
    else:
        printer("Invalid choice. Please try again.")
        main_menu()






if __name__ == "__main__":
    main()
