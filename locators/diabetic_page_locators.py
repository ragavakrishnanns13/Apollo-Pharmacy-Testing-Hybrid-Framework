from selenium.webdriver.common.by import By

class DiabeticPageLocators:
    health = (By.XPATH, '(//div[@class="sectionTop"])[1]')
    diabetic_care = (By.XPATH, '//a[@href="/shop-by-health-conditions/diabetic"]')
    first_product = (By.XPATH, '(//h2[contains(text(),"Apollo Pharmacy")])[1]')
    logo = (By.XPATH, '//div[@class="Footer_footerLogo__isTPQ"]')
    login = (By.XPATH, '//div[@class="Header_loginCta__27QWs"]')
    login_container = (By.CSS_SELECTOR, "div.Header_loginCta__27QWs[data-action='login']")
    phone_number = (By.XPATH, '//input[@class="newLogin_input__Jviae"]')
    icon = (By.XPATH, '//i[@class="icon-ic_arrow_forward newLogin_icon__Vz4jQ"]')
    verify_text = (By.XPATH, '//h2[text()="Now type in the OTP sent to"]')
    footerLogoApollo = (By.ID, "footerLogoBlock")
