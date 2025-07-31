import pytest
from time import sleep
from locators.location_page_locators import LocationPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.excel_utils import ExcelReader
from utilities.logger import setup_logger

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(7)
@pytest.mark.usefixtures("setup")
class TestLocationSelection:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes location selection and pharmacy navigation flow
        Return Type: None
        Parameters: None
        """
        self.click_address()
        self.choose_different_location()
        self.enter_location()
        self.select_hosur()
        self.click_pharmacy_near_me()
        self.enter_full_screen()

    def click_address(self):
        """
        Method Name: click_address
        Author: Ragava Krishnan
        Description: Clicks on the address section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LocationPageLocators.address)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="G")
            self.helper.verify(LocationPageLocators.address, expected_text)
            # self.helper.verify(LocationPageLocators.address, "Address")
            logger.info("Clicked on address.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error clicking address: {e}")
        Screenshot.take_screenshot()

    def choose_different_location(self):
        """
        Method Name: choose_different_location
        Author: Ragava Krishnan
        Description: Chooses a different location
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LocationPageLocators.choose_diff_loc)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="G")
            self.helper.verify(LocationPageLocators.choose_diff_loc, expected_text)
            # self.helper.verify(LocationPageLocators.choose_diff_loc, "Choose Different Location")
            logger.info("Chose different location.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error choosing different location: {e}")
        Screenshot.take_screenshot()

    def enter_location(self):
        """
        Method Name: enter_location
        Author: Ragava Krishnan
        Description: Enters a location into the input field
        Return Type: None
        Parameters: None
        """
        try:
            location = self.reader.read_data(sheet_name="input_data", row_number=1, column_name="A")
            self.helper.send_keys(LocationPageLocators.input, location)
            # self.helper.send_keys(LocationPageLocators.input, "Hosur")
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="G")
            self.helper.verify(LocationPageLocators.input, expected_text)
            # self.helper.verify(LocationPageLocators.input, "Location Input")
            logger.info("Entered location: Hosur.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error entering location: {e}")
        Screenshot.take_screenshot()

    def select_hosur(self):
        """
        Method Name: select_hosur
        Author: Ragava Krishnan
        Description: Selects Hosur from the location suggestions
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LocationPageLocators.hosur)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="G")
            self.helper.verify(LocationPageLocators.hosur, expected_text)
            # self.helper.verify(LocationPageLocators.hosur, "Hosur")
            logger.info("Selected Hosur.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error selecting Hosur: {e}")
        Screenshot.take_screenshot()

    def click_pharmacy_near_me(self):
        """
        Method Name: click_pharmacy_near_me
        Author: Ragava Krishnan
        Description: Clicks on the Pharmacy Near Me section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LocationPageLocators.pharmacy_near_me)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="G")
            self.helper.verify(LocationPageLocators.pharmacy_near_me, expected_text)
            # self.helper.verify(LocationPageLocators.pharmacy_near_me, "Pharmacy Near Me")
            logger.info("Clicked on Pharmacy Near Me.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error clicking Pharmacy Near Me: {e}")
        Screenshot.take_screenshot()

    def enter_full_screen(self):
        """
        Method Name: enter_full_screen
        Author: Ragava Krishnan
        Description: Enters full screen mode
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LocationPageLocators.full_screen)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="G")
            self.helper.verify(LocationPageLocators.full_screen, expected_text)
            # self.helper.verify(LocationPageLocators.full_screen, "Full Screen")
            logger.info("Entered full screen mode.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error entering full screen: {e}")
        Screenshot.take_screenshot()
