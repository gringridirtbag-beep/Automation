from selenium.webdriver.common.by import By
from core.waits import Waits
from utils.logger import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self,locator):
        try:
            logger.info(f"Click on {locator}")
            Waits.visible(self.driver, (By.CSS_SELECTOR,locator)).click()
        except Exception as e:
            logger.error(f"Error clicking {locator}: {e}", exc_info=True)
            raise
        

    def fill(self,locator,text):
        try:
            logger.info(f"typing into {locator} with text:{text}")
            Waits.visible(self.driver, (By.CSS_SELECTOR,locator)).send_keys(text)
        except Exception as e:
            logger.error(f"Error clicking {locator}: {e}", exc_info=True)
            raise 

    def get_url(self):
         current_url = self.driver.current_url
         logger.info(f"get url: {current_url}")
         return current_url

    def get_locator_text(self,locator):
        try:
            logger.info(f"get locator {locator}")
            locator_text = Waits.visible(self.driver,(By.CSS_SELECTOR,locator)).text
            print(locator_text)
            logger.info(f"Get locator text: {locator_text}")
        except Exception as e:
            logger.error(f"Error clicking {locator}: {e}", exc_info=True)
            raise 

        return locator_text


    def navigate_url(self,url):
         logger.info(f"Navigate to: {url}")
         self.driver.get(url)
    