import json
import random
from utils import get_user_choice, clear_screen, load_data_from_json

settings = load_data_from_json("data/settings.json")
perks_data = load_data_from_json("data/perks.json")
items_data = load_data_from_json("data/items.json")
addons_data = load_data_from_json("data/addons.json")
offerings_data = load_data_from_json("data/offerings.json")

def generate_random_survivor_build():
    # Gather all survivor perks
    all_perks = [perk for perks_list in perks_data["Survivor"].values() for perk in perks_list]
    selected_perks = random.sample(all_perks, 4)

    build = {"Perks": selected_perks}

    if settings['enable_survivor_items_and_addons']:
        # Gather all items including event items if enabled
        all_items = [item for items in items_data["Items"].values() for item in items]
        if settings.get('enable_event_items', True):
            all_items += [item for items in items_data["Event Items"].values() for item in items]

        # Randomly select an item
        selected_item = random.choice(all_items)
        build["Item"] = selected_item

        # Find the type of the selected item
        item_type = [type for type, items in items_data["Items"].items() if selected_item in items]
        if not item_type and settings.get('enable_event_items', True):
            item_type = [type for type, items in items_data["Event Items"].items() if selected_item in items]

        if item_type:
            item_type = item_type[0]
            # Gather all addons for the selected item type, including event addons if enabled
            all_addons = items_data["Addons"].get(f"{item_type}", [])
            if settings.get('enable_event_addons', True) and f"Event {item_type}" in items_data["Addons"]:
                all_addons += items_data["Addons"][f"Event {item_type}"]

            # Randomly select 2 addons for the item if there are any addons available
            if all_addons:
                selected_addons = random.sample(all_addons, min(2, len(all_addons)))
                build["Addons"] = selected_addons

    # Select a random offering if any offering setting is enabled
    if any(settings.get(key, False) for key in [
        'enable_big_bp_offerings',
        'enable_small_bp_offerings',
        'enable_map_offerings',
        'enable_map_modification_offerings',
        'enable_luck_offerings',
        'enable_ward_offerings',
        'enable_shroud_offerings',
        'enable_event_offerings'
    ]):
        filtered_offerings = filter_offerings(settings, "Survivor")
        if filtered_offerings:
            selected_offering = random.choice(filtered_offerings)
            build["Offering"] = selected_offering

    return build

def generate_random_killer_build():
    # Gather all killer perks, excluding "General Perks"
    all_perks = [perk for killer_perks in perks_data["Killer"].values() if killer_perks != "General Perks" for perk in killer_perks]
    selected_perks = random.sample(all_perks, 4)

    build = {"Perks": selected_perks}

    if settings['enable_killer_addons']:
        # Ask the user for the killer they are playing
        clear_screen()
        print("Select your chosen Killer:")
        killers = [killer for killer in perks_data["Killer"].keys() if killer != "General Perks"]
        for i, killer in enumerate(killers, start=1):
            print(f"{i}. {killer}")
        choice = get_user_choice(1, len(killers))
        selected_killer = killers[choice - 1]

        # Randomly select addons for the selected killer
        all_addons = addons_data.get(selected_killer, [])
        if all_addons:
            selected_addons = random.sample(all_addons, 2)
            build["Addons"] = selected_addons

    # Select a random offering if any offering setting is enabled
    if any(settings.get(key, False) for key in [
        'enable_big_bp_offerings',
        'enable_small_bp_offerings',
        'enable_map_offerings',
        'enable_map_modification_offerings',
        'enable_ward_offerings',
        'enable_shroud_offerings',
        'enable_mori_offerings',
        'enable_event_offerings'
    ]):
        filtered_offerings = filter_offerings(settings, "Killer")
        if filtered_offerings:
            selected_offering = random.choice(filtered_offerings)
            build["Offering"] = selected_offering

    return build

def filter_offerings(settings, role):
    offering_types = [
        "Big Bloodpoints",
        "Small Bloodpoints",
        "Maps",
        "Map Modifications",
        "Luck" if role == "Survivor" else None,
        "Wards",
        "Shrouds",
        "Moris" if role == "Killer" else None,
        "Event"
    ]
    
    enabled_settings = {
        "Big Bloodpoints": settings['enable_big_bp_offerings'],
        "Small Bloodpoints": settings['enable_small_bp_offerings'],
        "Maps": settings['enable_map_offerings'],
        "Map Modifications": settings['enable_map_modification_offerings'],
        "Luck": settings['enable_luck_offerings'] if role == "Survivor" else False,
        "Wards": settings['enable_ward_offerings'],
        "Shrouds": settings['enable_shroud_offerings'],
        "Moris": settings['enable_mori_offerings'] if role == "Killer" else False,
        "Event": settings['enable_event_offerings']
    }

    filtered_offerings = []
    for offering_type in offering_types:
        if offering_type and enabled_settings[offering_type]:
            filtered_offerings.extend(offerings_data[role][offering_type])

    return filtered_offerings