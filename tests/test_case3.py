from time import sleep

import pytest
from selenium.webdriver.common.by import By
from utilities.selenium_utils import switch_window, select_dropdown_option
from utilities.excel_utils import read_excel_data

@pytest.mark.usefixtures("driver")
class TestCase3:

    def test_navigation_and_operations(self, driver):
        # Example: Navigate to a webpage
        driver.get("https://www.homedepot.com/")
        driver.implicitly_wait(10)

        sleep(3)

        # test_data = read_excel_data("test_data/test_data.xlsx", "Sheet1")
        # print(test_data)

        # assert "Example Domain" in driver.title
