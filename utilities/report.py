import os
import datetime
import time
import shutil

class BeautifulReporter:
    """
    Class Name: Beautiful Reporter
    Author: Moksha Tej
    Description: Reporter utility, that uses pytest--html reporter with customisation
    Return Type: index.html
    Parameters: None
    """
    BASE_DIRECTORY = 'C:/Users/10835482/Desktop/CodingChallenges/Gladiator/Reports'
    REPORT_DIRECTORY = os.path.join(BASE_DIRECTORY, "BeautifulReports")

    def __init__(self):
        time.sleep(2)
        # Remove all contents of the REPORT_DIRECTORY if it exists
        if os.path.exists(self.REPORT_DIRECTORY):
            shutil.rmtree(self.REPORT_DIRECTORY)
        os.makedirs(self.REPORT_DIRECTORY, exist_ok=True)

    def generate_report(self):
        time.sleep(2)
        # Replace colons with hyphens to avoid Windows path errors
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        timestamped_folder = os.path.join(
            self.REPORT_DIRECTORY, f"BeautifulReports_{timestamp}"
        )
        os.makedirs(timestamped_folder, exist_ok=True)

        beautiful_command = (
            f"pytest --html={timestamped_folder}/report.html --self-contained-html"
        )
        os.system(beautiful_command)

        # Optional: Automatically open the report after generation
        report_path = os.path.join(timestamped_folder, "report.html")
        if os.path.exists(report_path):
            os.startfile(report_path)

        return report_path
