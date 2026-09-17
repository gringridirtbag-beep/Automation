from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Waits: 
    @staticmethod
    def visible(driver, locator, timeout = 10):
        return WebDriverWait(driver,timeout).until(expected_conditions.visibility_of_element_located(locator))