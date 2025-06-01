# Marvel Rivals Hero Snipe Tool

A utility that helps you quickly secure your preferred hero in Marvel Rivals before others can select it.

## Description

This tool gives you an edge in the hero selection race by instantly clicking when the yellow confirmation button appears. By automating the confirmation click, you can snipe heroes that other players might be planning to pick, ensuring you get your preferred character.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `pyautogui`
  - `Pillow` (PIL)

## Installation

1. Ensure Python is installed on your system
2. Install required packages:
   ```
   pip install pyautogui Pillow
   ```

## Usage

1. Run the script:
   ```
   python "Marvels Auto Confirm.py"
   ```
2. In the hero selection screen, quickly move your cursor over your desired hero
3. Position your cursor precisely where the yellow confirmation button will appear
4. When another player tries to select the same hero, or when you need to quickly confirm, the yellow button will appear and the tool will instantly click it
5. The program automatically exits after successfully sniping the hero

## How it Works

The script continuously monitors the RGB color value of the pixel under your cursor. When it detects the specific yellow color used by Marvel Rivals confirmation buttons (RGB: 232, 213, 74), it instantly performs a mouse click at that position - faster than human reaction time. This gives you an advantage in securing heroes that are in high demand.

## Tips

- Run the tool just before entering a match or during hero selection phase
- Pre-position your cursor where the confirmation button will appear for your desired hero
- For popular heroes that get picked quickly, this tool gives you a crucial speed advantage
- To abort the program at any time, press Ctrl+C
- Move your cursor to any corner of the screen to trigger PyAutoGUI's failsafe
- If the tool isn't detecting the button, you may need to adjust the COLOR_TOLERANCE value in the script

## Troubleshooting

- **Tool doesn't detect the button**: The exact color might vary slightly between systems. You can modify the TARGET_YELLOW value in the script if needed.
- **Error messages**: Make sure you have the required packages installed.

## Safety

This tool only performs mouse clicks. It has a failsafe mechanism - quickly move your cursor to any corner of the screen to abort.
