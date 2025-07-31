from selenium.webdriver.common.by import By

class ApolloProductsLocators:
    apollo_products = (By.XPATH, "//a[@href='/shop-by-category/apollo-products']")
    ors_drinks = (By.XPATH, "//span[text()='ORS Drinks']")
    sort_by = (By.XPATH, "//div[@class='ProductSortWeb_ddMain__34yMl']")
    price_low_to_high = (By.XPATH, "(//div[@class='ProductSortWeb_listRoot__r04MX'])[2]")
    add = (By.XPATH, "(//button[@aria-label='Add'])[1]")
    view_cart = (By.XPATH, "//span[text()='View Cart']")
    apollo_nav_icon_css = (By.CSS_SELECTOR, ".ApolloHeader_navIconPlaceholder")
    qty = (By.XPATH, "//div[@class='MedicineProductCard_optionHead__zOvKm']")
    five = (By.XPATH, "(//div[@class='MedicineProductCard_list__fe7Ub '])[2]")
    sort_dropdown = (By.ID, "sortActive")
    proceed = (By.XPATH, "//span[text()='Proceed']")
