import os
import ctypes
import json

def set_console_title():
    os.system("title DBD Randomizer - By Merky")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_screen():
    os.system('pause' if os.name == 'nt' else 'Press Enter to continue...')

def load_data_from_json(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        data = json.load(f)
    return data

def get_user_choice(min_choice, max_choice):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print("Invalid choice. Please enter a number between", min_choice, "and", max_choice)
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_survivor_build(build):
    clear_screen()
    print("============== PERKS ==============")
    for i, perk in enumerate(build["Perks"], start=1):
        print(f"Perk #{i}: {perk}")

    print("\n============== ITEM & ADDONS ==============")
    if "Item" in build:
        print(f"Item: {build['Item']}")
        if "Addons" in build:
            for i, addon in enumerate(build["Addons"], start=1):
                print(f"Addon #{i}: {addon}")
        else:
            print("Addons: None")
    else:
        print("Item: None")

    print("\n============== OFFERING ==============")
    print(f"Offering: {build.get('Offering', 'None')}")
    print("")

def print_killer_build(build):
    clear_screen()
    print("============== PERKS ==============")
    for i, perk in enumerate(build["Perks"], start=1):
        print(f"Perk #{i}: {perk}")

    print("\n============== ADDONS ==============")
    if "Addons" in build:
        for i, addon in enumerate(build["Addons"], start=1):
            print(f"Addon #{i}: {addon}")
    else:
        print("Addons: None")

    print("\n============== OFFERING ==============")
    print(f"Offering: {build.get('Offering', 'None')}")
    print("")
