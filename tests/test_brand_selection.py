import pytest
from locators.brands_page_locators import BrandsPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(9)
@pytest.mark.usefixtures("setup")
class TestBrandSelection:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes brand selection and offer verification flow in oral care section
        Return Type: None
        Parameters: None
        """
        self.scroll_to_browse_by()
        self.click_oral_care()
        self.select_brand()
        self.select_colgate()
        self.add_product()
        self.select_first_product()
        self.scroll_to_offers()
        self.verify_offers()

    def scroll_to_browse_by(self):
        """
        Method Name: scroll_to_browse_by
        Author: Ragava Krishnan
        Description: Scrolls to the 'Browse By' section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.scroll_to_element(BrandsPageLocators.browse_by)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="I")
            self.helper.verify(BrandsPageLocators.browse_by, expected_text)
            # self.helper.verify(BrandsPageLocators.browse_by, "Browse By")
            logger.info("Scrolled to 'Browse By' section.")
        except Exception as e:
            logger.error(f"Error scrolling to 'Browse By': {e}")
        Screenshot.take_screenshot()

    def click_oral_care(self):
        """
        Method Name: click_oral_care
        Author: Ragava Krishnan
        Description: Clicks on the Oral Care category
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.js_click_element(BrandsPageLocators.oral_care)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="I")
            self.helper.verify(BrandsPageLocators.oral_care, expected_text)
            # self.helper.verify(BrandsPageLocators.oral_care, "Oral Care")
            logger.info("Clicked on Oral Care.")
        except Exception as e:
            logger.error(f"Error clicking Oral Care: {e}")
        Screenshot.take_screenshot()

    def select_brand(self):
        """
        Method Name: select_brand
        Author: Ragava Krishnan
        Description: Clicks on the Brands filter
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(BrandsPageLocators.brands)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="I")
            self.helper.verify(BrandsPageLocators.brands, expected_text)
            # self.helper.verify(BrandsPageLocators.brands, "Brands")
            logger.info("Clicked on Brands.")
        except Exception as e:
            logger.error(f"Error clicking Brands: {e}")
        Screenshot.take_screenshot()

    def select_colgate(self):
        """
        Method Name: select_colgate
        Author: Ragava Krishnan
        Description: Selects Colgate brand from the filter
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(BrandsPageLocators.colgate)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="I")
            self.helper.verify(BrandsPageLocators.colgate, expected_text)
            # self.helper.verify(BrandsPageLocators.colgate, "Colgate")
            logger.info("Selected Colgate brand.")
        except Exception as e:
            logger.error(f"Error selecting Colgate: {e}")
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
            self.helper.click(BrandsPageLocators.add)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="I")
            self.helper.verify(BrandsPageLocators.add, expected_text)
            # self.helper.verify(BrandsPageLocators.add, "Add Product")
            logger.info("Added product to cart.")
        except Exception as e:
            logger.error(f"Error adding product: {e}")
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
            self.helper.click(BrandsPageLocators.first_product)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="I")
            self.helper.verify(BrandsPageLocators.first_product, expected_text)
            # self.helper.verify(BrandsPageLocators.first_product, "First Product")
            logger.info("Clicked on first product.")
        except Exception as e:
            logger.error(f"Error clicking first product: {e}")
        Screenshot.take_screenshot()

    def scroll_to_offers(self):
        """
        Method Name: scroll_to_offers
        Author: Ragava Krishnan
        Description: Scrolls to the Available Offers section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.scroll_to_element(BrandsPageLocators.available_offers)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=7, column_name="I")
            self.helper.verify(BrandsPageLocators.available_offers, expected_text)
            # self.helper.verify(BrandsPageLocators.available_offers, "Available Offers")
            logger.info("Scrolled to Available Offers.")
        except Exception as e:
            logger.error(f"Error scrolling to Available Offers: {e}")
        Screenshot.take_screenshot()

    def verify_offers(self):
        """
        Method Name: verify_offers
        Author: Ragava Krishnan
        Description: Verifies the Available Offers section
        Return Type: None
        Parameters: None
        """
        try:
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=8, column_name="I")
            self.helper.verify(BrandsPageLocators.available_offers, expected_text)
            # self.helper.verify(BrandsPageLocators.available_offers, "Available Offers")
            logger.info("Verified Available Offers section.")
        except Exception as e:
            logger.error(f"Error verifying Available Offers: {e}")
        Screenshot.take_screenshot()
