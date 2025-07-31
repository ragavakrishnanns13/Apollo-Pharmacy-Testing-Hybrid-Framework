from selenium.webdriver.common.by import By

class AskApolloLocators:
    scroll = (By.XPATH, "//h2[text()='NIVEA']")
    nivea_title = (By.CSS_SELECTOR, "h2.brandTitle[data-brand='NIVEA']")
    banner = (By.XPATH, '//a[@href="https://www.apollo247.com/ask-apollo"]')
    consult_button = (By.ID, "bookConsult_OnlinePrimary")
    doctor = (By.XPATH, '(//div[@class="chatMessagesStyles_topicItem__sshU_"])[2]')
    first_suggestion = (By.CSS_SELECTOR, "div.styles_suggestion__Product")
    first_option = (By.XPATH, '(//div[@class="false styles_suggestion__IaDSg"])[1]')
    book_now = (By.XPATH, '//span[text()="Book now"]')
    consult_online = (By.XPATH, "(//button[@value='bookVideoConsult'])[1]")



