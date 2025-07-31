import pytest
from time import sleep
from locators.appointment_page_locators import AppointmentPageLocators
from utilities.selenium_utils import SeleniumHelper
from utilities.screenshot import Screenshot
from utilities.logger import setup_logger
from utilities.excel_utils import ExcelReader

logger = setup_logger()

# @pytest.mark.skip
# @pytest.mark.order(5)
@pytest.mark.usefixtures("setup")
class TestDoctorAppointment:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.helper = SeleniumHelper(self.driver)
        self.reader = ExcelReader('C:/Users/10835482/Desktop/test_data_local.xlsx')

    def test_navigation_and_operations(self):
        """
        Method Name: test_navigation_and_operations
        Author: Ragava Krishnan
        Description: Executes doctor appointment flow and verifies error handling for invalid phone number
        Return Type: None
        Parameters: None
        """
        self.click_doctor_appointment()
        self.select_neurology()
        self.sort_by_relevance()
        self.sort_by_experience()
        self.click_consult()
        self.click_continue()
        self.enter_phone_number()
        self.verify_error_message()

    def click_doctor_appointment(self):
        """
        Method Name: click_doctor_appointment
        Author: Ragava Krishnan
        Description: Clicks on the Doctor Appointment section
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AppointmentPageLocators.doctor_appointment)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=1, column_name="E")
            self.helper.verify(AppointmentPageLocators.doctor_appointment, expected_text)
            # self.helper.verify(AppointmentPageLocators.doctor_appointment, "Doctor Appointment")
            logger.info("Clicked on Doctor Appointment.")
        except Exception as e:
            logger.error(f"Error clicking Doctor Appointment: {e}")
        Screenshot.take_screenshot()

    def select_neurology(self):
        """
        Method Name: select_neurology
        Author: Ragava Krishnan
        Description: Selects the Neurology specialty
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AppointmentPageLocators.neurology)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=2, column_name="E")
            self.helper.verify(AppointmentPageLocators.neurology, expected_text)
            # self.helper.verify(AppointmentPageLocators.neurology, "Neurology")
            logger.info("Selected Neurology.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error selecting Neurology: {e}")
        Screenshot.take_screenshot()

    def sort_by_relevance(self):
        """
        Method Name: sort_by_relevance
        Author: Ragava Krishnan
        Description: Sorts doctors by relevance
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AppointmentPageLocators.relevance)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=3, column_name="E")
            self.helper.verify(AppointmentPageLocators.relevance, expected_text)
            # self.helper.verify(AppointmentPageLocators.relevance, "Relevance")
            logger.info("Sorted by Relevance.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error sorting by Relevance: {e}")
        Screenshot.take_screenshot()

    def sort_by_experience(self):
        """
        Method Name: sort_by_experience
        Author: Ragava Krishnan
        Description: Sorts doctors by experience
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AppointmentPageLocators.experience)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=4, column_name="E")
            self.helper.verify(AppointmentPageLocators.experience, expected_text)
            # self.helper.verify(AppointmentPageLocators.experience, "Experience")
            logger.info("Sorted by Experience.")
            sleep(4)
        except Exception as e:
            logger.error(f"Error sorting by Experience: {e}")
        Screenshot.take_screenshot()

    def click_consult(self):
        """
        Method Name: click_consult
        Author: Ragava Krishnan
        Description: Clicks the Consult button
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AppointmentPageLocators.consult)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=5, column_name="E")
            self.helper.verify(AppointmentPageLocators.consult, expected_text)
            # self.helper.verify(AppointmentPageLocators.consult, "Consult")
            logger.info("Clicked on Consult.")
            sleep(2)
        except Exception as e:
            logger.error(f"Error clicking Consult: {e}")
        Screenshot.take_screenshot()

    def click_continue(self):
        """
        Method Name: click_continue
        Author: Ragava Krishnan
        Description: Clicks the Continue button
        Return Type: None
        Parameters: None
        """
        try:
            self.helper.click(AppointmentPageLocators.CONTINUE)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=6, column_name="E")
            self.helper.verify(AppointmentPageLocators.CONTINUE, expected_text)
            # self.helper.verify(AppointmentPageLocators.CONTINUE, "Continue")
            logger.info("Clicked Continue.")
        except Exception as e:
            logger.error(f"Error clicking Continue: {e}")
        Screenshot.take_screenshot()

    def enter_phone_number(self):
        """
        Method Name: enter_phone_number
        Author: Ragava Krishnan
        Description: Enters an invalid phone number
        Return Type: None
        Parameters: None
        """
        try:
            phone_number = self.reader.read_data(sheet_name="input_data", row_number=2, column_name="A")
            self.helper.send_keys(AppointmentPageLocators.phone_number_input, phone_number)
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=7, column_name="E")
            self.helper.verify(AppointmentPageLocators.phone_number_input, expected_text)
            # self.helper.verify(AppointmentPageLocators.phone_number_input, "Invalid Phone Number")
            logger.info("Entered phone number.")
        except Exception as e:
            logger.error(f"Error entering phone number: {e}")
        Screenshot.take_screenshot()

    def verify_error_message(self):
        """
        Method Name: verify_error_message
        Author: Ragava Krishnan
        Description: Verifies the error message for invalid phone number
        Return Type: None
        Parameters: None
        """
        try:
            expected_text = self.reader.read_data(sheet_name="verify_data", row_number=8, column_name="E")
            self.helper.verify(AppointmentPageLocators.error_msg, expected_text)
            # self.helper.verify(AppointmentPageLocators.error_msg, "This seems like a wrong number")
            logger.info("Verified error message for invalid phone number.")
        except Exception as e:
            logger.error(f"Error verifying error message: {e}")
        Screenshot.take_screenshot()



