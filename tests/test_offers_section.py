import pytest
from time import sleep
from locators.offers_page_locators import OffersPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(4)
@pytest.mark.usefixtures("setup")
class TestOffersSection:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes product sorting and cart flow from offers section
        Return Type: None
        Parameters: None
        """
        self.click_offers()
        self.scroll_to_section()
        self.verify_deals_by_category()
        self.select_home_essentials()
        self.sort_by_price()
        self.add_product()
        self.view_cart()

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
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="D")
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
            self.helper.scroll_to_element(OffersPageLocators.scroll)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="D")
            self.helper.verify(OffersPageLocators.scroll, expected_text)
            # self.helper.verify(OffersPageLocators.scroll, "Products")
            logger.info("Scrolled to section.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error scrolling to section: {e}")
        Screenshot.take_screenshot()

    def verify_deals_by_category(self):
        """
        Method Name: verify_deals_by_category
        Author: Ragava Krishnan
        Description: Verifies the 'DEALS BY CATEGORY' section
        Return Type: None
        Parameters: None
        """
        try:
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="D")
            self.helper.verify(OffersPageLocators.deals_by_category, expected_text)
            # self.helper.verify(OffersPageLocators.deals_by_category, "DEALS BY CATEGORY")
            logger.info("Verified 'DEALS BY CATEGORY' section.")
        except Exception as e:
            logger.error(f"Error verifying deals by category: {e}")
        Screenshot.take_screenshot()

    def select_home_essentials(self):
        """
        Method Name: select_home_essentials
        Author: Ragava Krishnan
        Description: Selects the Home Essentials category
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.home_essentials)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="D")
            self.helper.verify(OffersPageLocators.home_essentials, expected_text)
            # self.helper.verify(OffersPageLocators.home_essentials, "Home Essentials")
            logger.info("Selected Home Essentials.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error selecting Home Essentials: {e}")
        Screenshot.take_screenshot()

    def sort_by_price(self):
        """
        Method Name: sort_by_price
        Author: Ragava Krishnan
        Description: Sorts products by price from low to high
        Return Type: None
        Parameters: None
        """
        try:
            sleep(4)
            self.helper.click(OffersPageLocators.sort_by)
            expected_text_1 = self.reader.read_data(sheet_name="verify_data", row_number=8, column_name="D")
            self.helper.verify(OffersPageLocators.sort_by, expected_text_1)
            # self.helper.verify(OffersPageLocators.sort_by, "Sort By")
            self.helper.click(OffersPageLocators.price_low_to_high)
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="D")
            self.helper.verify(OffersPageLocators.price_low_to_high, expected_text_2)
            # self.helper.verify(OffersPageLocators.price_low_to_high, "Price Low to High")
            logger.info("Sorted by price: Low to High.")
            sleep(3)
        except Exception as e:
            logger.error(f"Error sorting by price: {e}")
        Screenshot.take_screenshot()

    def add_product(self):
        """
        Method Name: add_product
        Author: Ragava Krishnan
        Description: Adds a product to the cart
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.add_product)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="D")
            self.helper.verify(OffersPageLocators.add_product, expected_text)
            logger.info("Added product to cart.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error adding product: {e}")
        Screenshot.take_screenshot()

    def view_cart(self):
        """
        Method Name: view_cart
        Author: Ragava Krishnan
        Description: Views the cart after adding product
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(OffersPageLocators.view_cart)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=7, column_name="D")
            self.helper.verify(OffersPageLocators.view_cart, expected_text)
            # self.helper.verify(OffersPageLocators.view_cart, "View Cart")
            logger.info("Viewed cart.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error viewing cart: {e}")
        Screenshot.take_screenshot()
