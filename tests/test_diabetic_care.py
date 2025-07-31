import pytest
from time import sleep
from locators.diabetic_page_locators import DiabeticPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(12)
@pytest.mark.usefixtures("setup")
class TestDiabeticCare:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes diabetic care product selection and login flow
        Return Type: None
        Parameters: None
        """
        self.scroll_to_health()
        self.click_diabetic_care()
        self.select_first_product()
        self.click_login()
        self.enter_phone_number()

    def scroll_to_health(self):
        """
        Method Name: scroll_to_health
        Author: Ragava Krishnan
        Description: Scrolls to the Health section
        Return Type: None
        Parameters: None
        """
        try:
            sleep(4)
            self.helper.scroll_to_element(DiabeticPageLocators.health)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="L")
            self.helper.verify(DiabeticPageLocators.health, expected_text)
            # self.helper.verify(DiabeticPageLocators.health, "Health")
            logger.info("Scrolled to Health section.")
        except Exception as e:
            logger.error(f"Error scrolling to Health: {e}")
        Screenshot.take_screenshot()

    def click_diabetic_care(self):
        """
        Method Name: click_diabetic_care
        Author: Ragava Krishnan
        Description: Clicks on the Diabetic Care category
        Return Type: None
        Parameters: None
        """
        try:
            sleep(3)
            self.helper.js_click_element(DiabeticPageLocators.diabetic_care)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="L")
            self.helper.verify(DiabeticPageLocators.diabetic_care, expected_text)
            # self.helper.verify(DiabeticPageLocators.diabetic_care, "Diabetic Care")
            logger.info("Clicked on Diabetic Care.")
        except Exception as e:
            logger.error(f"Error clicking Diabetic Care: {e}")
        Screenshot.take_screenshot()

    def select_first_product(self):
        """
        Method Name: select_first_product
        Author: Ragava Krishnan
        Description: Selects the first product from the list
        Return Type: None
        Parameters: None
        """
        try:
            sleep(2)
            self.helper.click(DiabeticPageLocators.first_product)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="L")
            self.helper.verify(DiabeticPageLocators.first_product, expected_text)
            # self.helper.verify(DiabeticPageLocators.first_product, "Product")
            logger.info("Selected first product.")
        except Exception as e:
            logger.error(f"Error selecting first product: {e}")
        Screenshot.take_screenshot()

    def click_login(self):
        """
        Method Name: click_login
        Author: Ragava Krishnan
        Description: Clicks on the Login button
        Return Type: None
        Parameters: None
        """
        try:
            sleep(2)
            self.helper.click(DiabeticPageLocators.login)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="L")
            self.helper.verify(DiabeticPageLocators.login, expected_text)
            # self.helper.verify(DiabeticPageLocators.login, "Login")
            logger.info("Clicked on Login.")
        except Exception as e:
            logger.error(f"Error clicking Login: {e}")
        Screenshot.take_screenshot()

    def enter_phone_number(self):
        """
        Method Name: enter_phone_number
        Author: Ragava Krishnan
        Description: Enters phone number and clicks the icon to proceed
        Return Type: None
        Parameters: None
        """
        try:
            sleep(2)
            self.helper.click(DiabeticPageLocators.phone_number)
            expected_text_1 = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="L")
            self.helper.verify(DiabeticPageLocators.phone_number, expected_text_1)
            # self.helper.verify(DiabeticPageLocators.phone_number, "Phone Number")
            phone_number = self.reader.read_data(sheet_name="input_data", row_number=3, column_name="A")
            self.helper.send_keys(DiabeticPageLocators.phone_number, phone_number)
            # self.helper.send_keys(DiabeticPageLocators.phone_number, "8903405346")
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="L")
            self.helper.verify(DiabeticPageLocators.phone_number, expected_text_2)
            # self.helper.verify(DiabeticPageLocators.phone_number, "Enter Phone Number")
            self.helper.click(DiabeticPageLocators.icon)
            expected_text_3 = self.reader.read_data(sheet_name="verify_data", row_number=7, column_name="L")
            self.helper.verify(DiabeticPageLocators.icon, expected_text_3)
            # self.helper.verify(DiabeticPageLocators.icon, "Submit Icon")
            logger.info("Entered phone number and clicked icon.")
        except Exception as e:
            logger.error(f"Error entering phone number: {e}")
        Screenshot.take_screenshot()
