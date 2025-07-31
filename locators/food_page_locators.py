from selenium.webdriver.common.by import By

class FoodPageLocators:
    nutrition_header = (By.CSS_SELECTOR, "h2.Footer_title__5ve3Y[data-section='nutrition']")
    footer = (By.XPATH, '(//h2[@class="Footer_title__5ve3Y"])[6]')
    formula = (By.XPATH, '//a[@href="http://apollopharmacy.in/momverse/p/breastfeeding-and-formula"]')
    infant = (By.XPATH, '//a[@href="/momverse/c/newborn-and-infant"]')
    baby_food = (By.XPATH, '//a[@href="/momverse/p/baby-food"]//div[@class="MenuWeb_leftSection__fqPNx"]')
    read_section = (By.XPATH, '(//div[@class="RelatedArticles_title__Krqk5 "])[1]')
    infant_care_card = (By.ID, "tileInfantNewborn01")
    view_all = (By.XPATH, '//a[@href="/momverse/resources/articles?p=baby-food&t=food-nutrition"]')
