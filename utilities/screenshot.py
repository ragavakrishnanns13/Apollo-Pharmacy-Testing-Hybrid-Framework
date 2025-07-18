import os
from datetime import datetime
import pyautogui

def take_screenshot():
    # Create 'screenshots' directory if it doesn't exist
    folder = 'screenshots'
    os.makedirs(folder, exist_ok=True)

    # Generate a timestamped filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screenshot_{timestamp}.png'
    filepath = os.path.join(folder, filename)

    # Take screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot saved to {filepath}")

# Example usage
if __name__ == "__main__":
    take_screenshot()
