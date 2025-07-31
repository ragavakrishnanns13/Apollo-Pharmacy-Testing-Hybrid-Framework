import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    configobj = ConfigReader()
    url = configobj.get_url()
    driver.get(url)

    yield driver

    driver.quit()








