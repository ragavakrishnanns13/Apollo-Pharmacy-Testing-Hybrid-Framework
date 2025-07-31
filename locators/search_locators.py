from selenium.webdriver.common.by import By

class SearchLocators:
    search_bar = (By.XPATH, "//div[@class='SearchPlaceholder_sRoot__ZK2aL']")
    search_input = (By.XPATH, "//input[@placeholder='Search medicines, brands and more']")
    first_product = (By.XPATH, "//a[@href='/otc/nivea-fresh-active-rollon-for-men-50ml?doNotTrack=true']")
    ml_change = (By.XPATH, "(//section[@class='_h'])[2]")
    scroll = (By.XPATH, "//div[@class='Rn']")
    search_container = (By.CSS_SELECTOR, "div.SearchPlaceholder_sRoot__ZK2aL[data-component='search']")
    add_to_cart_text = (By.ID, "addCartTextSpan")
    search_input_field = (By.CSS_SELECTOR, "input[placeholder='Search medicines, brands and more'][data-role='input']")
    add_to_cart = (By.XPATH, "//span[text()='Add to Cart']")
    view_cart = (By.XPATH, "//span[@class='Qp']")
    last_minute_buys = (By.XPATH, "//div[@class='CartLanding_peopleBoughtSection__ELcCN']")
