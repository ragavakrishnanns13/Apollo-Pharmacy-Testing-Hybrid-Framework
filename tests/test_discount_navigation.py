import pytest
from time import sleep
from locators.discount_page_locators import DiscountPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(13)
@pytest.mark.usefixtures("setup")
class TestDiscountNavigation:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self, stock=None):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes discount navigation and product addition flow
        Return Type: None
        Parameters: stock (optional): Boolean to determine if stock is available
        """
        self.click_discount()
        self.scroll_to_category()
        self.click_home()
        self.scroll_to_add()
        self.click_add_buttons(stock)

    def click_discount(self):
        """
        Method Name: click_discount
        Author: Ragava Krishnan
        Description: Clicks on the Discount section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(DiscountPageLocators.discount)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="M")
            self.helper.verify(DiscountPageLocators.discount, expected_text)
            # self.helper.verify(DiscountPageLocators.discount, "Discount")
            logger.info("Clicked on Discount.")
        except Exception as e:
            logger.error(f"Error clicking Discount: {e}")
        Screenshot.take_screenshot()

    def scroll_to_category(self):
        """
        Method Name: scroll_to_category
        Author: Ragava Krishnan
        Description: Scrolls to the Category section
        Return Type: None
        Parameters: None
        """
        try:
            sleep(3)
            self.helper.js_scroll(DiscountPageLocators.category)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="M")
            self.helper.verify(DiscountPageLocators.category, expected_text)
            # self.helper.verify(DiscountPageLocators.category, "Category")
            logger.info("Scrolled to Category.")
        except Exception as e:
            logger.error(f"Error scrolling to Category: {e}")
        Screenshot.take_screenshot()

    def click_home(self):
        """
        Method Name: click_home
        Author: Ragava Krishnan
        Description: Clicks on the Home category
        Return Type: None
        Parameters: None
        """
        try:
            sleep(2)
            self.helper.click(DiscountPageLocators.home)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="M")
            self.helper.verify(DiscountPageLocators.home, expected_text)
            # self.helper.verify(DiscountPageLocators.home, "Home")
            logger.info("Clicked on Home.")
        except Exception as e:
            logger.error(f"Error clicking Home: {e}")
        Screenshot.take_screenshot()

    def scroll_to_add(self):
        """
        Method Name: scroll_to_add
        Author: Ragava Krishnan
        Description: Scrolls to the Add button section
        Return Type: None
        Parameters: None
        """
        try:
            sleep(6)
            self.helper.js_scroll(DiscountPageLocators.add)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="M")
            self.helper.verify(DiscountPageLocators.add, expected_text)
            # self.helper.verify(DiscountPageLocators.add, "Add Button")
            logger.info("Scrolled to Add button.")
        except Exception as e:
            logger.error(f"Error scrolling to Add: {e}")
        Screenshot.take_screenshot()

    def click_add_buttons(self, stock):
        """
        Method Name: click_add_buttons
        Author: Ragava Krishnan
        Description: Clicks on Add buttons based on stock availability
        Return Type: None
        Parameters: stock (optional): Boolean to determine if stock is available
        """
        try:
            if stock:
                self.helper.js_click_element(DiscountPageLocators.add)
                expected_text_1 = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="M")
                self.helper.verify(DiscountPageLocators.add, expected_text_1)
                # self.helper.verify(DiscountPageLocators.add, "Add Button (Stock Available)")
                logger.info("Clicked on Add button (stock available).")
            sleep(2)
            self.helper.js_click_element(DiscountPageLocators.add_not_available)
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="M")
            self.helper.verify(DiscountPageLocators.add_not_available, expected_text_2)
            # self.helper.verify(DiscountPageLocators.add_not_available, "Add Button (No Stock Available)")
            logger.info("Clicked on second Add button.")
        except Exception as e:
            logger.error(f"Error clicking Add buttons: {e}")
        Screenshot.take_screenshot()
