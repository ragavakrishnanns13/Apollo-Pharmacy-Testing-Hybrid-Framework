from selenium.webdriver.common.by import By

class OffersPageLocators:
    offers = (By.XPATH, "//a[@class='Header_icon____pQe icon-offers']")
    product_section = (By.XPATH, "//div[@class='TopDealsFeatureBrands_sliderMainBlock__3iTmL']")
    pampers = (By.XPATH, "(//p[@class='TopDealsFeatureBrands_proTitle__Q3XnX'])[2]")
    add_to_cart = (By.XPATH, "(//button[@aria-label='Button'])[1]")
    view_cart = (By.XPATH, "//a[@class='Header_icon____pQe Header_cart__Pwy9_ icon-cart_icon']")
    my_cart = (By.XPATH, "//li[text()='MY CART']")
    deals_header = (By.CSS_SELECTOR, "h2[data-title='Deals By Category']")
    scroll = (By.XPATH, "//div[@class='DealsByCategory_sliderMainBlock__OMXZw']")
    deals_by_category = (By.XPATH, "//h2[text()='Deals By Category']")
    home_essentials = (By.XPATH, "(//a[@href='/shop-by-category/home-essentials'])[2]")
    sort_by = (By.XPATH, "(//button[@aria-label='Button'])[2]")
    sort_price_low_high = (By.ID, "priceSort_lowToHigh")
    add_product_btn = (By.ID, "btnAddProduct_02")
    price_low_to_high = (By.XPATH, "(//div[@class='ProductSortWeb_listRoot__r04MX'])[2]")
    add_product = (By.XPATH, "(//button[@aria-label='Add'])[2]")


