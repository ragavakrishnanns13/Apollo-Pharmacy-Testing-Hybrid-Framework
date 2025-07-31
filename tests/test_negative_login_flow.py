import pytest
from time import sleep
from locators.login_page_locators import LoginPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(2)
@pytest.mark.usefixtures("setup")
class TestNegativeLoginFLow:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes login flow with invalid phone number and verifies error handling
        Return Type: None
        Parameters: None
        """
        self.click_login()
        self.click_phone_number_div()
        self.enter_invalid_phone_number()
        self.verify_wrong_number_message()
        self.close_popup()
        self.click_whatsapp()

    def click_login(self):
        """
        Method Name: click_login
        Author: Ragava Krishnan
        Description: Clicks the login button on the homepage
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LoginPageLocators.login)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="B")
            self.helper.verify(LoginPageLocators.login, expected_text)
            # self.helper.verify(LoginPageLocators.login, "login")
            logger.info("Clicked login button.")
        except Exception as e:
            logger.error(f"Error clicking login button: {e}")
        Screenshot.take_screenshot()

    def click_phone_number_div(self):
        """
        Method Name: click_phone_number_div
        Author: Ragava Krishnan
        Description: Clicks the phone number input section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LoginPageLocators.phone_number_div)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="B")
            self.helper.verify(LoginPageLocators.phone_number_div, expected_text)
            # self.helper.verify(LoginPageLocators.phone_number_div, "mobile number")
            logger.info("Clicked phone number div.")
        except Exception as e:
            logger.error(f"Error clicking phone number div: {e}")
        Screenshot.take_screenshot()

    def enter_invalid_phone_number(self):
        """
        Method Name: enter_invalid_phone_number
        Author: Ragava Krishnan
        Description: Enters an invalid phone number into the input field
        Return Type: None
        Parameters: None
        """
        try:
            phone_number = self.reader.read_data(sheet_name="input_data", row_number=2, column_name="A")
            self.helper.send_keys(LoginPageLocators.phone_number_input, phone_number)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="B")
            self.helper.verify(LoginPageLocators.phone_number_input, expected_text)
            # self.helper.verify(LoginPageLocators.phone_number_input, "invalid number")
            logger.info("Entered invalid phone number.")
        except Exception as e:
            logger.error(f"Error entering phone number: {e}")
        Screenshot.take_screenshot()

    def verify_wrong_number_message(self):
        """
        Method Name: verify_wrong_number_message
        Author: Ragava Krishnan
        Description: Verifies the error message for wrong phone number
        Return Type: None
        Parameters: None
        """
        try:
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="B")
            self.helper.verify(LoginPageLocators.wrong_number, expected_text)
            # self.helper.verify(LoginPageLocators.wrong_number, "This seems like a wrong number")
            logger.info("Verified wrong number message.")
        except Exception as e:
            logger.error(f"Error verifying wrong number message: {e}")
        Screenshot.take_screenshot()

    def close_popup(self):
        """
        Method Name: close_popup
        Author: Ragava Krishnan
        Description: Closes the error message pop-up
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LoginPageLocators.close_pop_up)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="B")
            self.helper.verify(LoginPageLocators.close_pop_up, expected_text)
            # self.helper.verify(LoginPageLocators.close_pop_up, "close pop-up")
            logger.info("Closed pop-up.")
            sleep(3)
        except Exception as e:
            logger.error(f"Error closing pop-up: {e}")
        Screenshot.take_screenshot()

    def click_whatsapp(self):
        """
        Method Name: click_whatsapp
        Author: Ragava Krishnan
        Description: Clicks the WhatsApp button
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LoginPageLocators.whatsapp)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="B")
            self.helper.verify(LoginPageLocators.whatsapp, expected_text)
            # self.helper.verify(LoginPageLocators.whatsapp, "WhatsApp")
            logger.info("Clicked WhatsApp button.")
        except Exception as e:
            logger.error(f"Error clicking WhatsApp button: {e}")
            logger.warning("WhatsApp is blocked.")
        Screenshot.take_screenshot()
