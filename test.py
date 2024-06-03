import pyautogui
from settings import load_settings

settings = load_settings()

print(settings['item_inventory_position'])
pyautogui.moveTo(settings['item_inventory_position'])

# print(pyautogui.position())