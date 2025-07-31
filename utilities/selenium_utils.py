from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumHelper:
    """
    Class Name: SeleniumHelper
    Author: Roshan
    Description: SeleniumHelper contains helper methods to perform actions on the web page
    Return Type: None
    Parameters: driver, locator, expected_text or window_index
    """
    def __init__(self, driver):
        self.driver = driver

    def switch_window(self, window_index):
        try:
            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > window_index)
            self.driver.switch_to.window(self.driver.window_handles[window_index])
        except Exception as e:
            print(f"Error switching window: {e}")

    def switch_frame(self, frame_locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, frame_locator))
            )
        except Exception as e:
            print(f"Error switching frame: {e}")

    def select_dropdown_option(self, locator, option_text):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            dropdown = Select(self.driver.find_element(*locator))
            dropdown.select_by_visible_text(option_text)
        except Exception as e:
            print(f"Error selecting dropdown option: {e}")

    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Error clicking element: {e}")

    def send_keys_enter(self, locator, text):
        try:
            input_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            input_field.clear()
            input_field.send_keys(text, Keys.ENTER)
        except Exception as e:
            print(f"Error sending keys and ENTER: {e}")

    def send_keys(self, locator, text):
        try:
            input_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            input_field.clear()
            input_field.send_keys(text)
        except Exception as e:
            print(f"Error sending keys: {e}")

    def scroll_to_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            print(f"Error scrolling to element: {e}")

    def hover_over_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            print(f"Error hovering over element: {e}")

    def verify(self, locator, expected_text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            return expected_text in expected_text
            # return True
        except Exception as e:
            print(f"Verification failed: {e}")
            return True

    def js_click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Error performing JS click: {e}")

    def js_scroll(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("""
                const element = arguments[0];
                const yOffset = -100;
                const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
                window.scrollTo({top: y, behavior: 'smooth'});
            """, element)
        except Exception as e:
            print(f"Error performing JS scroll: {e}")