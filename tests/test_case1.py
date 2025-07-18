from time import sleep
from locators.locators1 import Locators1
import pytest
from selenium.webdriver.common.by import By
from utilities.selenium_utils import *
from utilities.screenshot import take_screenshot
from utilities.excel_utils import read_excel_data

@pytest.mark.usefixtures("driver")
class TestCase1:

    def test_navigation_and_operations(self, driver):
        # Navigate to the webpage
        driver.get("https://www.homedepot.com/")
        driver.implicitly_wait(10)

#       click on shop all
        click(driver, Locators1.shop_all_div)

#       click on savings
        click(driver, Locators1.savings_span)

#       click on all savings
        click(driver, Locators1.shop_all_savings_span)

#       click on grills
        scroll_to_element(driver, Locators1.scroll_1)
        click(driver, Locators1.grills_div)

#       take a screenshot
        take_screenshot()



