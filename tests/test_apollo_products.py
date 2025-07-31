import pytest
from time import sleep
from locators.apollo_products_locators import ApolloProductsLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(6)
@pytest.mark.usefixtures("setup")
class TestApolloProducts:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes product selection, cart update, and checkout flow
        Return Type: None
        Parameters: None
        """
        self.hover_apollo_products()
        self.select_ors_drinks()
        self.sort_by_price()
        self.add_product()
        self.view_cart()
        self.change_quantity()
        self.proceed_to_checkout()

    def hover_apollo_products(self):
        """
        Method Name: hover_apollo_products
        Author: Ragava Krishnan
        Description: Hovers over Apollo Products menu
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.hover_over_element(ApolloProductsLocators.apollo_products)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="F")
            self.helper.verify(ApolloProductsLocators.apollo_products, expected_text)
            # self.helper.verify(Locators6.apollo_products, "Apollo Products")
            logger.info("Hovered over Apollo Products.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error hovering over Apollo Products: {e}")
        Screenshot.take_screenshot()

    def select_ors_drinks(self):
        """
        Method Name: select_ors_drinks
        Author: Ragava Krishnan
        Description: Selects ORS Drinks category
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(ApolloProductsLocators.ors_drinks)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="F")
            self.helper.verify(ApolloProductsLocators.ors_drinks, expected_text)
            # self.helper.verify(Locators6.ors_drinks, "ORS Drinks")
            logger.info("Selected ORS Drinks.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error selecting ORS Drinks: {e}")
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
            self.helper.click(ApolloProductsLocators.sort_by)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="F")
            self.helper.verify(ApolloProductsLocators.sort_by, expected_text)
            # self.helper.verify(Locators6.sort_by, "Sort By")
            sleep(2)
            self.helper.click(ApolloProductsLocators.price_low_to_high)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="F")
            self.helper.verify(ApolloProductsLocators.price_low_to_high, expected_text)
            # self.helper.verify(Locators6.price_low_to_high, "Price Low to High")
            logger.info("Sorted by price: Low to High.")
            sleep(2)
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
            self.helper.click(ApolloProductsLocators.add)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="F")
            self.helper.verify(ApolloProductsLocators.add, expected_text)
            # self.helper.verify(Locators6.add, "Add Product")
            logger.info("Added product to cart.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error adding product: {e}")
        Screenshot.take_screenshot()

    def view_cart(self):
        """
        Method Name: view_cart
        Author: Ragava Krishnan
        Description: Views the cart
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(ApolloProductsLocators.view_cart)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="F")
            self.helper.verify(ApolloProductsLocators.view_cart, expected_text)
            # self.helper.verify(Locators6.view_cart, "View Cart")
            logger.info("Viewed cart.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error viewing cart: {e}")
        Screenshot.take_screenshot()

    def change_quantity(self):
        """
        Method Name: change_quantity
        Author: Ragava Krishnan
        Description: Changes product quantity in cart
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(ApolloProductsLocators.qty)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=7, column_name="F")
            self.helper.verify(ApolloProductsLocators.qty, expected_text)
            # self.helper.verify(Locators6.qty, "Quantity Dropdown")
            sleep(2)
            self.helper.click(ApolloProductsLocators.five)
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=8, column_name="F")
            self.helper.verify(ApolloProductsLocators.five, expected_text_2)
            # self.helper.verify(ApolloProductsLocators.five, "Quantity 5")
            logger.info("Changed quantity to 5.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error changing quantity: {e}")
        Screenshot.take_screenshot()

    def proceed_to_checkout(self):
        """
        Method Name: proceed_to_checkout
        Author: Ragava Krishnan
        Description: Proceeds to checkout
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(ApolloProductsLocators.proceed)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=9, column_name="F")
            self.helper.verify(ApolloProductsLocators.proceed, expected_text)
            # self.helper.verify(Locators6.proceed, "Proceed to Checkout")
            logger.info("Proceeded to checkout.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error proceeding to checkout: {e}")
        Screenshot.take_screenshot()
