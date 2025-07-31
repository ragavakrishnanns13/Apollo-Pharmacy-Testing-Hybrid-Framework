from selenium.webdriver.common.by import By

class LocationPageLocators:
    address = (By.XPATH, "//div[@class='LocationSearch_locationRoot__nTSCU']")
    choose_diff_loc = (By.XPATH, "//span[text()='Choose a different location']")
    input = (By.XPATH, "//input[@placeholder='Search for society, locality, pincode...']")
    hosur = (By.XPATH, "(//div[@class='NewSearchLocationSuggestor_searchItemList__9UqR6'])[1]")
    pharmacy_near_me = (By.XPATH, "//h2[text()='Pharmacy Near Me']")
    full_screen = (By.XPATH, "//button[@aria-label='Toggle fullscreen view']")
    alternate_location = (By.CSS_SELECTOR, "span[data-action='change-location']")
    search_input = (By.ID, "LocationSearchInput")
    hosur_title = (By.ID, "LocationSuggestItem01")


