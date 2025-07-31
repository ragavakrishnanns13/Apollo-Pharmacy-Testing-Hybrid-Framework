import pytest
from time import sleep
from locators.food_page_locators import FoodPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.excel_utils import ExcelReader
from utilities.logger import setup_logger

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(10)
@pytest.mark.usefixtures("setup")
class TestProductCategory:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes footer navigation, window switch, and product category flow
        Return Type: None
        Parameters: None
        """
        self.scroll_to_footer()
        self.click_formula()
        self.switch_to_new_window()
        self.hover_infant()
        self.click_baby_food()
        self.scroll_to_read_section()
        self.click_view_all()

    def scroll_to_footer(self):
        """
        Method Name: scroll_to_footer
        Author: Ragava Krishnan
        Description: Scrolls to the footer section
        Return Type: None
        Parameters: None
        """
        try:
            sleep(4)
            self.helper.scroll_to_element(FoodPageLocators.footer)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="J")
            self.helper.verify(FoodPageLocators.footer, expected_text)
            # self.helper.verify(FoodPageLocators.footer, "Footer")
            logger.info("Scrolled to footer.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error scrolling to footer: {e}")
        Screenshot.take_screenshot()

    def click_formula(self):
        """
        Method Name: click_formula
        Author: Ragava Krishnan
        Description: Clicks on the Formula link in the footer
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(FoodPageLocators.formula)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="J")
            self.helper.verify(FoodPageLocators.formula, expected_text)
            # self.helper.verify(FoodPageLocators.formula, "Formula")
            logger.info("Clicked on Formula.")
        except Exception as e:
            logger.error(f"Error clicking Formula: {e}")
        Screenshot.take_screenshot()

    def switch_to_new_window(self):
        """
        Method Name: switch_to_new_window
        Author: Ragava Krishnan
        Description: Switches to the newly opened browser window
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.switch_window(1)
            logger.info("Switched to new window.")
        except Exception as e:
            logger.error(f"Error switching window: {e}")
        Screenshot.take_screenshot()

    def hover_infant(self):
        """
        Method Name: hover_infant
        Author: Ragava Krishnan
        Description: Hovers over the Infant category
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.hover_over_element(FoodPageLocators.infant)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="J")
            self.helper.verify(FoodPageLocators.infant, expected_text)
            # self.helper.verify(FoodPageLocators.infant, "Infant")
            logger.info("Hovered over Infant.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error hovering over Infant: {e}")
        Screenshot.take_screenshot()

    def click_baby_food(self):
        """
        Method Name: click_baby_food
        Author: Ragava Krishnan
        Description: Clicks on the Baby Food category
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(FoodPageLocators.baby_food)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="J")
            self.helper.verify(FoodPageLocators.baby_food, expected_text)
            # self.helper.verify(FoodPageLocators.baby_food, "Baby Food")
            logger.info("Clicked on Baby Food.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error clicking Baby Food: {e}")
        Screenshot.take_screenshot()

    def scroll_to_read_section(self):
        """
        Method Name: scroll_to_read_section
        Author: Ragava Krishnan
        Description: Scrolls to the Read Section on the page
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.js_scroll(FoodPageLocators.read_section)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="J")
            self.helper.verify(FoodPageLocators.read_section, expected_text)
            # self.helper.verify(FoodPageLocators.read_section, "Read Section")
            logger.info("Scrolled to Read Section.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error scrolling to Read Section: {e}")
        Screenshot.take_screenshot()

    def click_view_all(self):
        """
        Method Name: click_view_all
        Author: Ragava Krishnan
        Description: Clicks on the View All button
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(FoodPageLocators.view_all)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="J")
            self.helper.verify(FoodPageLocators.view_all, expected_text)
            # self.helper.verify(FoodPageLocators.view_all, "View All")
            logger.info("Clicked on View All.")
        except Exception as e:
            logger.error(f"Error clicking View All: {e}")
        Screenshot.take_screenshot()
