from selenium.webdriver.common.by import By

class LoginPageLocators:
    login = (By.XPATH, "//div[@class='Header_loginCta__27QWs']")
    phone_number_div = (By.XPATH, "//div[@class='newLogin_phoneInput__0N3nu']")
    phone_number_input = (By.XPATH, "//input[@class='newLogin_input__Jviae']")
    submit = (By.XPATH, "(//button[@aria-label='Button'])[2]")
    whatsapp_redirect_link = (By.ID, "whatsappOrderCTA")
    otp_digit_1 = (By.XPATH, "//input[@data-val='1']")
    otp_digit_2 = (By.XPATH, "//input[@data-val='2']")
    otp_digit_3 = (By.XPATH, "//input[@data-val='3']")
    otp_digit_4 = (By.XPATH, "//input[@data-val='4']")
    otp_digit_5 = (By.XPATH, "//input[@data-val='5']")
    otp_digit_6 = (By.XPATH, "//input[@data-val='6']")
    submit_btn = (By.ID, "submitButtonLogin")
    wrong_number = (By.XPATH, "//p[text()='This seems like a wrong number']")
    close_pop_up = (By.XPATH, "//span[@aria-label='close button']")
    phone_input_container = (By.CSS_SELECTOR, "div.newLogin_phoneInput__0N3nu[data-type='phone']")
    whatsapp = (By.XPATH, "//a[@href='https://wa.me/919355247247?text=Order_medicines']")
