from selenium import webdriver 

class Driver :

    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver



