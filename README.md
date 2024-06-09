# Dead by Daylight Build Randomizer

## Description
This Python script generates random builds for the game Dead by Daylight. It allows users to generate random Survivor or Killer builds and adjust settings such as auto-applying the build and enabling/disabling various in-game features.

## Features
- Randomly generate Dead by Daylight builds for both Killer and Survivor up to v.8.0.0 (Vecna Release).
- Enable many toggleable settings to include and exclude different types of perks, items, and addons.
- Automatically apply builds to your character in a matter of seconds.

## Requirements
- Python 3.6 or higher
- pyautogui
- Other dependencies listed in requirements.txt

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/DBD-Randomizer.git
    cd DBD-Randomizer
    ```

2. **Install the Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Script**:
    ```sh
    python main.py
    ```

## Usage
1. **Configure Settings**: Adjust settings in `settings.json` as needed.
2. **Run the Script**: Use the command `python main.py` to generate and apply random builds.
3. **Follow On-Screen Instructions**: The script will guide you through the process of generating and applying builds.

## Troubleshooting
- **FileNotFoundError**: Ensure that the `data` directory and its contents are correctly placed and accessible.
- **Dependency Issues**: Verify that all required dependencies are installed. Use `pip list` to check installed packages.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
