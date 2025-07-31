from selenium.webdriver.common.by import By

class DiscountPageLocators:
    discount = (By.XPATH, '//a[@class="Header_icon____pQe icon-offers"]')
    category = (By.XPATH, '//h2[text()="Deals By Category"]')
    home = (By.XPATH, '(//a[@href="/shop-by-category/home-essentials"])[2]')
    home_essentials = (By.ID, "linkHomeEssentials_2")
    view_cart_link = (By.CSS_SELECTOR, "span[data-action='View Cart']")
    add = (By.XPATH, '(//div[@class="mb "])[1]')
    deals_category_header = (By.CSS_SELECTOR, "h2[data-label='Deals By Category']")
    add_not_available = (By.XPATH, '(//div[@class="mb "])[2]')
    view_cart = (By.XPATH, '//span[text()="View Cart"]')
