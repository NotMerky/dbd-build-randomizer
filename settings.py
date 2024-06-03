import json
import pyautogui
import time
from utils import clear_screen, pause_screen, get_user_choice
# from apply import calibrate_mouse

SETTINGS_FILE = "data/settings.json"

def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default settings if file doesn't exist
        return {
            "auto_apply_build": False,
            "print_build": True,
            "enable_survivor_items_and_addons": True,
            "enable_event_items": False,
            "enable_event_addons": False,
            "enable_killer_addons": True,
            "enable_big_bp_offerings": True,
            "enable_small_bp_offerings": False,
            "enable_map_offerings": True,
            "enable_map_modification_offerings": True,
            "enable_luck_offerings": True,
            "enable_ward_offerings": True,
            "enable_shroud_offerings": True,
            "enable_mori_offerings": True,
            "enable_event_offerings": False
        }
    
def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def adjust_settings():
    settings = load_settings()
    while True:
        clear_screen()
        print("===== Settings =====")
        print("[1] Program Settings")
        print("[2] Items & Addons Settings")
        print("[3] Offerings Settings")
        print("[4] Calibrate Auto Apply")
        print("[5] Restore Default Settings")
        print("[6] Back\n")

        choice = get_user_choice(1, 6)

        if choice == 1:
            adjust_program_settings(settings)
        elif choice == 2:
            adjust_items_addons_settings(settings)
        elif choice == 3:
            adjust_offerings_settings(settings)
        elif choice == 4:
            calibrate_mouse(settings)
        elif choice == 5:
            restore_default_settings(settings)
        elif choice == 6:
            save_settings(settings)
            print("\nSettings saved.\n")
            pause_screen()
            break

def adjust_program_settings(settings):
    while True:
        clear_screen()
        print("===== Program Settings =====")
        print("[1] Auto Apply Random Loadout (Currently:", "Enabled)" if settings['auto_apply_build'] else "Disabled)")
        print("[2] Print Loadout After Creating Random Build (Currently:", "Enabled)" if settings['print_build'] else "Disabled)")
        print("[3] Back\n")

        choice = get_user_choice(1, 3)

        if choice == 1:
            settings['auto_apply_build'] = not settings['auto_apply_build']
        elif choice == 2:
            settings['print_build'] = not settings['print_build']
        elif choice == 3:
            break

def adjust_items_addons_settings(settings):
    while True:
        clear_screen()
        print("===== Items & Addons Settings =====")
        print("[1] Survivor Items & Addons (Currently:", "Enabled)" if settings['enable_survivor_items_and_addons'] else "Disabled)")
        print("[2] Event Items (Currently:", "Enabled)" if settings['enable_event_items'] else "Disabled)")
        print("[3] Event Addons (Currently:", "Enabled)" if settings['enable_event_addons'] else "Disabled)")
        print("[4] Killer Addons (Currently:", "Enabled)" if settings['enable_killer_addons'] else "Disabled)")
        print("[5] Back\n")

        choice = get_user_choice(1, 5)

        if choice == 1:
            settings['enable_survivor_items_and_addons'] = not settings['enable_survivor_items_and_addons']
        elif choice == 2:
            settings['enable_event_items'] = not settings['enable_event_items']
        elif choice == 3:
            settings['enable_event_addons'] = not settings['enable_event_addons']
        elif choice == 4:
            settings['enable_killer_addons'] = not settings['enable_killer_addons']
        elif choice == 5:
            break

def adjust_offerings_settings(settings):
    while True:
        clear_screen()
        print("===== Offerings Settings =====")
        print("[1] Big Bloodpoints Offerings (Currently:", "Enabled)" if settings['enable_big_bp_offerings'] else "Disabled)")
        print("[2] Small Bloodpoints Offerings (Currently:", "Enabled)" if settings['enable_small_bp_offerings'] else "Disabled)")
        print("[3] Map Offerings (Currently:", "Enabled)" if settings['enable_map_offerings'] else "Disabled)")
        print("[4] Map Modifications Offerings (Currently:", "Enabled)" if settings['enable_map_modification_offerings'] else "Disabled)")
        print("[5] Luck Offerings (Currently:", "Enabled)" if settings['enable_luck_offerings'] else "Disabled)")
        print("[6] Wards Offerings (Currently:", "Enabled)" if settings['enable_ward_offerings'] else "Disabled)")
        print("[7] Shrouds Offerings (Currently:", "Enabled)" if settings['enable_shroud_offerings'] else "Disabled)")
        print("[8] Moris Offerings (Currently:", "Enabled)" if settings['enable_mori_offerings'] else "Disabled)")
        print("[9] Event Offerings (Currently:", "Enabled)" if settings['enable_event_offerings'] else "Disabled)")
        print("[10] Back\n")

        choice = get_user_choice(1, 10)

        if choice == 1:
            settings['enable_big_bp_offerings'] = not settings['enable_big_bp_offerings']
        elif choice == 2:
            settings['enable_small_bp_offerings'] = not settings['enable_small_bp_offerings']
        elif choice == 3:
            settings['enable_map_offerings'] = not settings['enable_map_offerings']
        elif choice == 4:
            settings['enable_map_modification_offerings'] = not settings['enable_map_modification_offerings']
        elif choice == 5:
            settings['enable_luck_offerings'] = not settings['enable_luck_offerings']
        elif choice == 6:
            settings['enable_ward_offerings'] = not settings['enable_ward_offerings']
        elif choice == 7:
            settings['enable_shroud_offerings'] = not settings['enable_shroud_offerings']
        elif choice == 8:
            settings['enable_mori_offerings'] = not settings['enable_mori_offerings']
        elif choice == 9:
            settings['enable_event_offerings'] = not settings['enable_event_offerings']
        elif choice == 10:
            break

def calibrate_mouse(settings):
    clear_screen()
    print("Starting Calibration Sequence...")
    print("You will be prompted to move your mouse to a specified HUD element for the next few seconds.")
    print("Simply move your mouse to the specified region and wait for confirmation to move onto the next element.")
    print("Once you press any key the program will allow you 5 seconds to move to the first element, which is the first perk position.")
    pause_screen()
    
    print("\n[1/11] Move your mouse over to the First Perk Slot!")
    time.sleep(5)
    settings['first_perk_position'] = pyautogui.position()
    print("Recorded position for First Perk at:", settings['first_perk_position'])
    
    print("\n[2/11] Move your mouse over to the Second Perk Slot!")
    time.sleep(5)
    settings['second_perk_position'] = pyautogui.position()
    print("Recorded position for Second Perk at:", settings['second_perk_position'])
    
    print("\n[3/11] Move your mouse over to the Third Perk Slot!")
    time.sleep(5)
    settings['third_perk_position'] = pyautogui.position()
    print("Recorded position for Third Perk at:", settings['third_perk_position'])
    
    print("\n[4/11] Move your mouse over to the Fourth Perk Slot!")
    time.sleep(5)
    settings['fourth_perk_position'] = pyautogui.position()
    print("Recorded position for Fourth Perk at:", settings['fourth_perk_position'])
    
    print("\n[5/11] Move your mouse over to the Search Bar!")
    time.sleep(5)
    settings['search_bar_position'] = pyautogui.position()
    print("Recorded position for the Search Bar at:", settings['search_bar_position'])
    
    print("\n[6/11] Move your mouse over to the Item Slot!")
    time.sleep(5)
    settings['item_position'] = pyautogui.position()
    print("Recorded position for Item Slot at:", settings['item_position'])
    
    print("\n[7/11] Move your mouse over to the First Addon Slot!")
    time.sleep(5)
    settings['first_addon_position'] = pyautogui.position()
    print("Recorded position for the First Addon Slot at:", settings['first_addon_position'])
    
    print("\n[8/11] Move your mouse over to the Second Addon Slot!")
    time.sleep(5)
    settings['second_addon_position'] = pyautogui.position()
    print("Recorded position for the Second Addon Slot at:", settings['second_addon_position'])
    
    print("\n[9/11] Move your mouse over to the Offering Slot!")
    time.sleep(5)
    settings['offering_position'] = pyautogui.position()
    print("Recorded position for the Offering Slot at:", settings['offering_position'])
    
    print("\n[10/11] Move your mouse over to the First Perk/Offering in your Inventory!")
    time.sleep(5)
    settings['inventory_position'] = pyautogui.position()
    print("Recorded position for the Inventory Position at:", settings['inventory_position'])

    print("\n[11/11] Move your mouse over to the First Item/Addon in your Inventory!")
    time.sleep(5)
    settings['item_inventory_position'] = pyautogui.position()
    print("Recorded position for the Inventory Position at:", settings['item_inventory_position'])

    save_settings(settings)
    print("\nCalibration complete and saved.")

def restore_default_settings(settings):
    settings['auto_apply_build'] = False
    settings['print_build'] = True
    settings['enable_survivor_items_and_addons'] = True
    settings['enable_event_items'] = False
    settings['enable_event_addons'] = False
    settings['enable_killer_addons'] = True
    settings['enable_big_bp_offerings'] = True
    settings['enable_small_bp_offerings'] = False
    settings['enable_map_offerings'] = True
    settings['enable_map_modification_offerings'] = True
    settings['enable_luck_offerings'] = True
    settings['enable_ward_offerings'] = True
    settings['enable_shroud_offerings'] = True
    settings['enable_mori_offerings'] = True
    settings['enable_event_offerings'] = False
    settings['first_perk_position'] = [363, 416]
    settings['second_perk_position'] = [527, 416]
    settings['third_perk_position'] = [691, 416]
    settings['fourth_perk_position'] = [846, 416]
    settings['search_bar_position'] = [737, 525]
    settings['item_position'] = [347, 252]
    settings['first_addon_position'] = [514, 252]
    settings['second_addon_position'] = [600, 252]
    settings['offering_position'] = [790, 252]
    settings['inventory_position'] = [346, 609]
    settings['item_inventory_position'] = [430, 609]
    save_settings(settings)
    print("Default Settings Restored.")
    pause_screen()