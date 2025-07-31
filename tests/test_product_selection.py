import pytest
from time import sleep
from locators.offers_page_locators import OffersPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(3)
@pytest.mark.usefixtures("setup")
class TestProductSelection:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes product selection and cart verification flow
        Return Type: None
        Parameters: None
        """
        self.click_offers()
        self.scroll_to_section()
        self.select_pampers()
        self.add_to_cart()
        self.view_cart()
        self.verify_cart()

    def click_offers(self):
        """
        Method Name: click_offers
        Author: Ragava Krishnan
        Description: Clicks on the offers section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.offers)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="C")
            self.helper.verify(OffersPageLocators.offers, expected_text)
            # self.helper.verify(OffersPageLocators.offers, "offers")
            logger.info("Clicked on offers.")
        except Exception as e:
            logger.error(f"Error clicking offers: {e}")
        Screenshot.take_screenshot()

    def scroll_to_section(self):
        """
        Method Name: scroll_to_section
        Author: Ragava Krishnan
        Description: Scrolls to the product section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.scroll_to_element(OffersPageLocators.product_section)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="C")
            self.helper.verify(OffersPageLocators.product_section, expected_text)
            # self.helper.verify(OffersPageLocators.product_section, "Products")
            logger.info("Scrolled to section.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error scrolling to section: {e}")
        Screenshot.take_screenshot()

    def select_pampers(self):
        """
        Method Name: select_pampers
        Author: Ragava Krishnan
        Description: Selects the Pampers product
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.pampers)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="C")
            self.helper.verify(OffersPageLocators.pampers, expected_text)
            # self.helper.verify(OffersPageLocators.pampers, "Pampers")
            logger.info("Selected Pampers product.")
        except Exception as e:
            logger.error(f"Error selecting Pampers: {e}")
        Screenshot.take_screenshot()

    def add_to_cart(self):
        """
        Method Name: add_to_cart
        Author: Ragava Krishnan
        Description: Adds the selected product to the cart
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.add_to_cart)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="C")
            self.helper.verify(OffersPageLocators.add_to_cart, expected_text)
            # self.helper.verify(OffersPageLocators.add_to_cart, "Add to Cart")
            logger.info("Clicked add to cart.")
        except Exception as e:
            logger.error(f"Error adding to cart: {e}")
        Screenshot.take_screenshot()

    def view_cart(self):
        """
        Method Name: view_cart
        Author: Ragava Krishnan
        Description: Navigates to the cart view
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.view_cart)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="C")
            self.helper.verify(OffersPageLocators.view_cart, expected_text)
            # self.helper.verify(OffersPageLocators.view_cart, "View Cart")
            logger.info("Clicked view cart.")
        except Exception as e:
            logger.error(f"Error viewing cart: {e}")
        Screenshot.take_screenshot()

    def verify_cart(self):
        """
        Method Name: verify_cart
        Author: Ragava Krishnan
        Description: Verifies the cart page
        Return Type: None
        Parameters: None
        """
        try:
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="C")
            self.helper.verify(OffersPageLocators.my_cart, expected_text)
            # self.helper.verify(OffersPageLocators.my_cart, "MY CART")
            logger.info("Verified cart page.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error verifying cart: {e}")
        Screenshot.take_screenshot()
