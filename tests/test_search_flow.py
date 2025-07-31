import pytest
from time import sleep
from locators.search_locators import SearchLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(8)
@pytest.mark.usefixtures("setup")
class TestSearchFlow:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes product search, selection, variant change, and cart flow
        Return Type: None
        Parameters: None
        """
        self.search_product()
        self.select_product()
        self.change_variant()
        self.scroll_and_add_to_cart()
        self.view_cart()
        self.scroll_last_minute_buys()

    def search_product(self):
        """
        Method Name: search_product
        Author: Ragava Krishnan
        Description: Searches for a product using the search bar
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(SearchLocators.search_bar)
            expected_text_1 = self.reader.read_data(sheet_name="verify_data", row_number=1,column_name="H")
            self.helper.verify(SearchLocators.search_bar, expected_text_1)
            # self.helper.verify(SearchLocators.search_bar, "Search Bar")
            product_name = self.reader.read_data(sheet_name="input_data", row_number=5, column_name="A")
            self.helper.send_keys(SearchLocators.search_input, product_name)
            # self.helper.send_keys(SearchLocators.search_input, "Nivea Under Arm Men")
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="H")
            self.helper.verify(SearchLocators.search_input, expected_text_2)
            # self.helper.verify(SearchLocators.search_input, "Search Input")
            logger.info("Searched for 'Nivea Under Arm Men'.")
        except Exception as e:
            logger.error(f"Error searching product: {e}")
        Screenshot.take_screenshot()

    def select_product(self):
        """
        Method Name: select_product
        Author: Ragava Krishnan
        Description: Selects the first product from the search results
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(SearchLocators.first_product)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="H")
            self.helper.verify(SearchLocators.first_product, expected_text)
            # self.helper.verify(SearchLocators.first_product, "Product")
            logger.info("Selected first product.")
        except Exception as e:
            logger.error(f"Error selecting product: {e}")
        Screenshot.take_screenshot()

    def change_variant(self):
        """
        Method Name: change_variant
        Author: Ragava Krishnan
        Description: Changes the product variant (e.g., ml size)
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(SearchLocators.ml_change)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="H")
            self.helper.verify(SearchLocators.ml_change, expected_text)
            # self.helper.verify(SearchLocators.ml_change, "25ML")
            logger.info("Changed ml variant.")
            sleep(3)
        except Exception as e:
            logger.error(f"Error changing ml variant: {e}")
        Screenshot.take_screenshot()

    def scroll_and_add_to_cart(self):
        """
        Method Name: scroll_and_add_to_cart
        Author: Ragava Krishnan
        Description: Scrolls to the add-to-cart button and adds the product
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.scroll_to_element(SearchLocators.scroll)
            expected_text_1 = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="H")
            self.helper.verify(SearchLocators.scroll, expected_text_1)
            # self.helper.verify(SearchLocators.scroll, "Scroll Target")
            sleep(3)
            self.helper.click(SearchLocators.add_to_cart)
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="H")
            self.helper.verify(SearchLocators.add_to_cart, expected_text_2)
            # self.helper.verify(SearchLocators.add_to_cart, "Add to Cart")
            logger.info("Added product to cart.")
            sleep(3)
        except Exception as e:
            logger.error(f"Error adding to cart: {e}")
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
            self.helper.click(SearchLocators.view_cart)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=7, column_name="H")
            self.helper.verify(SearchLocators.view_cart, expected_text)
            # self.helper.verify(SearchLocators.view_cart, "View Cart")
            logger.info("Viewed cart.")
        except Exception as e:
            logger.error(f"Error viewing cart: {e}")
        Screenshot.take_screenshot()

    def scroll_last_minute_buys(self):
        """
        Method Name: scroll_last_minute_buys
        Author: Ragava Krishnan
        Description: Scrolls to the Last Minute Buys section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.scroll_to_element(SearchLocators.last_minute_buys)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=8, column_name="H")
            self.helper.verify(SearchLocators.last_minute_buys, expected_text)
            # self.helper.verify(SearchLocators.last_minute_buys, "Last Minute Buys")
            logger.info("Scrolled to Last Minute Buys.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error scrolling to Last Minute Buys: {e}")
        Screenshot.take_screenshot()
