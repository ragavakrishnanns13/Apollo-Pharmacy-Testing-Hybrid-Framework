import pytest
from time import sleep
from locators.ask_apollo_locators import AskApolloLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(11)
@pytest.mark.usefixtures("setup")
class TestAskApollo:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes banner interaction and doctor consultation flow
        Return Type: None
        Parameters: None
        """
        self.scroll_and_click_banner()
        self.click_doctor()
        self.select_first_option()
        self.scroll_and_book()
        self.consult_online()

    def scroll_and_click_banner(self):
        """
        Method Name: scroll_and_click_banner
        Author: Ragava Krishnan
        Description: Scrolls to and clicks on the banner
        Return Type: None
        Parameters: None
        """
        try:
            sleep(4)
            self.helper.scroll_to_element(AskApolloLocators.scroll)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="K")
            self.helper.verify(AskApolloLocators.scroll, expected_text)
            # self.helper.verify(AskApolloLocators.scroll, "Ask Apollo")
            sleep(4)
            self.helper.click(AskApolloLocators.banner)
            expected_text_2 = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="K")
            self.helper.verify(AskApolloLocators.banner, expected_text_2)
            # self.helper.verify(AskApolloLocators.banner, "Banner")
            logger.info("Scrolled and clicked on banner.")
        except Exception as e:
            logger.error(f"Error in scroll_and_click_banner: {e}")
        Screenshot.take_screenshot()

    def click_doctor(self):
        """
        Method Name: click_doctor
        Author: Ragava Krishnan
        Description: Clicks on the doctor option
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AskApolloLocators.doctor)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="K")
            self.helper.verify(AskApolloLocators.doctor, expected_text)
            # self.helper.verify(AskApolloLocators.doctor, "Doctor")
            logger.info("Clicked on doctor.")
        except Exception as e:
            logger.error(f"Error clicking doctor: {e}")
        Screenshot.take_screenshot()

    def select_first_option(self):
        """
        Method Name: select_first_option
        Author: Ragava Krishnan
        Description: Selects the first available option
        Return Type: None
        Parameters: None
        """
        try:
            sleep(3)
            self.helper.click(AskApolloLocators.first_option)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="K")
            self.helper.verify(AskApolloLocators.first_option, expected_text)
            # self.helper.verify(AskApolloLocators.first_option, "Option")
            logger.info("Selected first option.")
        except Exception as e:
            logger.error(f"Error selecting first option: {e}")
        Screenshot.take_screenshot()

    def scroll_and_book(self):
        """
        Method Name: scroll_and_book
        Author: Ragava Krishnan
        Description: Scrolls to and clicks the 'Book Now' button
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.scroll_to_element(AskApolloLocators.book_now)
            self.helper.click(AskApolloLocators.book_now)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="K")
            self.helper.verify(AskApolloLocators.book_now, expected_text)
            # self.helper.verify(AskApolloLocators.book_now, "Book Now")
            logger.info("Scrolled to and clicked 'Book Now'.")
        except Exception as e:
            logger.error(f"Error in scroll_and_book: {e}")
        Screenshot.take_screenshot()

    def consult_online(self):
        """
        Method Name: consult_online
        Author: Ragava Krishnan
        Description: Clicks on the 'Consult Online' button
        Return Type: None
        Parameters: None
        """
        try:
            sleep(4)
            self.helper.click(AskApolloLocators.consult_online)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="K")
            self.helper.verify(AskApolloLocators.consult_online, expected_text)
            # self.helper.verify(AskApolloLocators.consult_online, "Consult Online")
            sleep(2)
            logger.info("Clicked on 'Consult Online'.")
        except Exception as e:
            logger.error(f"Error clicking 'Consult Online': {e}")
        Screenshot.take_screenshot()
