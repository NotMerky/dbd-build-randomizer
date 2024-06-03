import pyautogui
import time
from utils import clear_screen, pause_screen
from settings import load_settings, save_settings

settings = load_settings()

def apply_build(build):
    # Moves mouse into window and focueses it
    pyautogui.move(0, 0)
    pyautogui.click()

    # Perks
    apply_perk(build["Perks"][0], settings['first_perk_position'])
    apply_perk(build["Perks"][1], settings['second_perk_position'])
    apply_perk(build["Perks"][2], settings['third_perk_position'])
    apply_perk(build["Perks"][3], settings['fourth_perk_position'])
    
    # Items & Addon
    if "Item" in build and "Addons" in build:
        apply_item(build["Item"])
        apply_addons(build["Addons"])

    elif "Addons" in build:
        apply_addons(build["Addons"])

    # Offering
    if "Offering" in build:
        apply_offering(build["Offering"])


def apply_perk(perk_name, perk_position):
    # Move mouse to the specified perk slot and click
    pyautogui.moveTo(perk_position)
    pyautogui.click()
    time.sleep(1)

    # Click on the search bar
    pyautogui.moveTo(settings['search_bar_position'])
    pyautogui.click()
    time.sleep(1)

    # Type the perk name and press Enter
    pyautogui.write(perk_name)
    pyautogui.press('enter')
    time.sleep(1)

    # Click on the first perk in the inventory
    pyautogui.moveTo(settings['inventory_position'])
    pyautogui.click()
    time.sleep(1)

def apply_item(item_name):
    # Move mouse to the item slot and click
    pyautogui.moveTo(settings['item_position'])
    pyautogui.click()
    time.sleep(1)

    # Click on the search bar
    pyautogui.moveTo(settings['search_bar_position'])
    pyautogui.click()
    time.sleep(1)

    # Type the item name and press Enter
    pyautogui.write(item_name)
    pyautogui.press('enter')
    time.sleep(1)

    # Click on the first item in the inventory
    pyautogui.moveTo(settings['item_inventory_position'])
    pyautogui.click()
    time.sleep(1)

def apply_addons(addons):
    # Move mouse to the first addon slot and click
    pyautogui.moveTo(settings['first_addon_position'])
    pyautogui.click()
    time.sleep(1)

    # Click on the search bar
    pyautogui.moveTo(settings['search_bar_position'])
    pyautogui.click()
    time.sleep(1)

    # Type the offering name and press Enter
    pyautogui.write(addons[0])
    pyautogui.press('enter')
    time.sleep(1)

    # Click on the first offering in the inventory
    pyautogui.moveTo(settings['item_inventory_position'])
    pyautogui.click()
    time.sleep(1)

    # Move mouse to the second addon slot and click
    pyautogui.moveTo(settings['second_addon_position'])
    pyautogui.click()
    time.sleep(1)

    # Click on the search bar
    pyautogui.moveTo(settings['search_bar_position'])
    pyautogui.click()
    time.sleep(1)

    # Type the offering name and press Enter
    pyautogui.write(addons[1])
    pyautogui.press('enter')
    time.sleep(1)

    # Click on the first offering in the inventory
    pyautogui.moveTo(settings['item_inventory_position'])
    pyautogui.click()
    time.sleep(1)

def apply_offering(offering_name):
    # Move mouse to the offering slot and click
    pyautogui.moveTo(settings['offering_position'])
    pyautogui.click()
    time.sleep(1)

    # Click on the search bar
    pyautogui.moveTo(settings['search_bar_position'])
    pyautogui.click()
    time.sleep(1)

    # Type the offering name and press Enter
    pyautogui.write(offering_name)
    pyautogui.press('enter')
    time.sleep(1)

    # Click on the first offering in the inventory
    pyautogui.moveTo(settings['inventory_position'])
    pyautogui.click()
    time.sleep(1)