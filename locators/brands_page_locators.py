from selenium.webdriver.common.by import By

class BrandsPageLocators:
    browse_by = (By.XPATH, "(//div[@class='sectionTop'])[1]")
    oral_care = (By.XPATH, "(//div[@class='T'])[6]")
    brands = (By.XPATH, "(//div[@class='Zv '])[1]")
    colgate = (By.XPATH, "//label[text()='colgate']")
    featured_product_card = (By.ID, "productCard_featured")
    add = (By.XPATH, "(//button[@aria-label='Add'])[1]")
    first_product = (By.XPATH, "(//a[@class='cardAnchorStyle'])[1]")
    colgate_option = (By.CSS_SELECTOR, "label[for='colgate']")
    scroll = (By.XPATH, "(//div[@class='jn '])[4]")
    available_offers = (By.XPATH, "//p[text()='Available Offers']")


