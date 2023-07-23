import slash as slash
from selenium import webdriver
import time


class BookingBaseTest(slash.Test):
    def __init__(self, test_method_name, fixture_store, fixture_namespace, variation):
        super().__init__(test_method_name, fixture_store, fixture_namespace, variation)
        self.driver = None

    def before(self):
        super().before()
        self.driver = webdriver.Chrome()

    def after(self):
        slash.logger.info("Closing Browser")
        self.driver.quit()
        slash.logger.info("Completed test")

    def open_landing_page(self):
        slash.logger.info("Opening booking.com")
        self.driver.get("https://www.booking.com")
