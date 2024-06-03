from build import generate_random_survivor_build, generate_random_killer_build
from utils import clear_screen, pause_screen, get_user_choice, set_console_title, print_survivor_build, print_killer_build
from settings import adjust_settings, load_settings
from apply import apply_build

def main():
    set_console_title("DBD Build Randomizer by Merky")
    while True:
        settings = load_settings()
        clear_screen()
        print("===== Dead by Daylight Perk Randomizer by Merky =====")
        print("[1] Generate Random Survivor Build")
        print("[2] Generate Random Killer Build")
        print("[3] Adjust Settings")
        print("[4] Exit Program\n")

        choice = get_user_choice(1, 4)

        if choice == 1:
            build = generate_random_survivor_build()
            if settings['print_build']:
                print_survivor_build(build)
            if settings['auto_apply_build']:
                apply_build(build)
            pause_screen()
            
        elif choice == 2:
            build = generate_random_killer_build()
            if settings['print_build']:
                print_killer_build(build)
            if settings['auto_apply_build']:
                apply_build(build)
            pause_screen()

        elif choice == 3:
            adjust_settings()
        
        elif choice == 4:
            break

if __name__ == "__main__":
    main()