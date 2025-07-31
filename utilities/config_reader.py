import configparser
from selenium import webdriver

class ConfigReader:
    """
    Class Name: ConfigReader
    Author: Muhilan
    Description: Reads data from config.properties, used for abstraction purpose
    Return Type: String
    Parameters: None
    """
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('C:/Users/10835482/Desktop/CodingChallenges/Gladiator/config/config.properties')

    def get_url(self):
        return self.config['DEFAULT']['url']

    def get_browser_command(self, browser_key='google_browser'):
        return self.config['DEFAULT'].get(browser_key)

    def get_driver(self, browser_key='google_browser'):
        browser_name = self.get_browser_command(browser_key)

        if browser_name.lower() == 'chrome':
            return webdriver.Chrome()
        elif browser_name.lower() == 'edge':
            return webdriver.Edge()
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
