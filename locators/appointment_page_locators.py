from selenium.webdriver.common.by import By

class AppointmentPageLocators:
    doctor_appointment = (By.XPATH, "(//a[@href='https://www.apollo247.com/specialties'])[1]")
    neurology = (By.XPATH, "(//div[@class='CollapsibleGrid_Item__JHSpl'])[6]")
    relevance = (By.ID, "headlessui-listbox-button-:r0:")
    filter = (By.ID, "filter_id")
    experience = (By.XPATH, "//span[text()='Years of Experience']")
    consult = (By.XPATH, "(//button[@value='bookVideoConsult'])[1]")
    CONTINUE = (By.XPATH, "//span[text()='Continue']")
    continue_btn_css = (By.CSS_SELECTOR, "button.continueSession")
    phone_number_input = (By.XPATH, "//input[@title='Please enter mobile number']")
    error_msg = (By.XPATH, "//div[@class='SignIn_helperText__zSmE_ SignIn_errorText__iIxpb']")


