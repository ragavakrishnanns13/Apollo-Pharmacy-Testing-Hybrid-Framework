import mss
import datetime
import os

class Screenshot:
    """
    Class Name: Screenshot
    Author: Ragava Krishnan
    Description: MSS library is used to take screenshot while testing
    Return Type: screenshot.png
    Parameters: None
    """
    @staticmethod
    def take_screenshot(name="", screenshot_dir = "C:/Users/10835482/Desktop/CodingChallenges/Gladiator/screenshots"):

        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_dir = screenshot_dir
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")

        with mss.mss() as sct:
            sct.shot(output=file_path)

        return file_path
