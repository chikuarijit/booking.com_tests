import slash
from . import constants as const
from . import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support import \
    expected_conditions as EC
import time


class Search:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):
        if not self.loaded():
            button = self.driver.find_element(By.CSS_SELECTOR, "div.f9cf783bde button[type='submit']")
            button.click()
        else:
            slash.logger.info("Search Page already loaded")

    def loaded(self):
        try:
            # Wait for the "properties found" string to be present in the page content
            utils.get_wait(self.driver).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1.f6431b446c"), "properties found")
            )
            return True
        except:
            return False
