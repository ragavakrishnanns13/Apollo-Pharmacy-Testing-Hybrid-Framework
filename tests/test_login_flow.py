import pytest
from time import sleep
from locators.login_page_locators import LoginPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(1)
@pytest.mark.usefixtures("setup")
class TestLoginFlow:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes login flow including phone number entry and OTP submission
        Return Type: None
        Parameters: None
        """
        self.click_login()
        self.click_phone_number_div()
        self.enter_phone_number()
        self.click_submit_button()
        self.enter_otp_digits()
        self.final_submit()

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
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="A")
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
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="A")
            self.helper.verify(LoginPageLocators.phone_number_div, expected_text)
            # self.helper.verify(LoginPageLocators.phone_number_div, "mobile number")
            logger.info("Clicked phone number div.")
        except Exception as e:
            logger.error(f"Error clicking phone number div: {e}")
        Screenshot.take_screenshot()

    def enter_phone_number(self):
        """
        Method Name: enter_phone_number
        Author: Ragava Krishnan
        Description: Enters the phone number into the input field
        Return Type: None
        Parameters: None
        """
        try:
            phone_number = self.reader.read_data(sheet_name="input_data", row_number=3, column_name="A")
            self.helper.send_keys(LoginPageLocators.phone_number_input, phone_number)
            # self.helper.send_keys(LoginPageLocators.phone_number_input, "8903405346")
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="A")
            self.helper.verify(LoginPageLocators.phone_number_input, expected_text)
            # self.helper.verify(LoginPageLocators.phone_number_input, "signing up")
            logger.info("Entered phone number.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error entering phone number: {e}")
        Screenshot.take_screenshot()

    def click_submit_button(self):
        """
        Method Name: click_submit_button
        Author: Ragava Krishnan
        Description: Clicks the submit button after entering phone number
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LoginPageLocators.submit)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="A")
            self.helper.verify(LoginPageLocators.submit, expected_text)
            # self.helper.verify(LoginPageLocators.submit, "Submit")
            logger.info("Clicked submit button.")
        except Exception as e:
            logger.error(f"Error clicking submit button: {e}")
        Screenshot.take_screenshot()

    def enter_otp_digits(self):
        """
        Method Name: enter_otp_digits
        Author: Ragava Krishnan
        Description: Enters OTP digits into respective input fields
        Return Type: None
        Parameters: None
        """
        try:
            otp_digits = [
                (LoginPageLocators.otp_digit_1, "1"),
                (LoginPageLocators.otp_digit_2, "2"),
                (LoginPageLocators.otp_digit_3, "3"),
                (LoginPageLocators.otp_digit_4, "4"),
                (LoginPageLocators.otp_digit_5, "5"),
                (LoginPageLocators.otp_digit_6, "6"),
            ]
            for locator, digit in otp_digits:
                self.helper.send_keys(locator, digit)
                expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="A")
                self.helper.verify(locator, expected_text)
                # self.helper.verify(locator, "OTP")
            logger.info("Entered OTP digits.")
        except Exception as e:
            logger.error(f"Error entering OTP digits: {e}")
        Screenshot.take_screenshot()

    def final_submit(self):
        """
        Method Name: final_submit
        Author: Ragava Krishnan
        Description: Clicks the final submit button after OTP entry
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(LoginPageLocators.submit)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="A")
            self.helper.verify(LoginPageLocators.submit, expected_text)
            # self.helper.verify(LoginPageLocators.submit, "Submit")
            logger.info("Clicked final submit button.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error clicking final submit: {e}")
        Screenshot.take_screenshot()
