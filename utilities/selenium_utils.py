from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def switch_window(driver, window_index):
    windows = driver.window_handles
    driver.switch_to.window(windows[window_index])

def switch_frame(driver, frame_locator):
    frame = WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, frame_locator))
    )

def select_dropdown_option(driver, locator, option_text):
    dropdown = Select(driver.find_element(*locator))
    dropdown.select_by_visible_text(option_text)

def click_checkbox(driver, locator):
    checkbox = driver.find_element(*locator)
    if not checkbox.is_selected():
        checkbox.click()

def click(driver, locator):
    option_button = driver.find_element(*locator)
    option_button.click()

def send_keys_enter(driver, locator, text):
    input_field = driver.find_element(*locator)
    input_field.clear()
    input_field.send_keys(text, Keys.ENTER)

def send_keys(driver, locator, text):
    input_field = driver.find_element(*locator)
    input_field.clear()
    input_field.send_keys(text)

def scroll_to_element(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)





    

