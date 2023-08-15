import slash as slash
from selenium import webdriver


class BookingBaseTest(slash.Test):
    def __init__(self, test_method_name, fixture_store, fixture_namespace, variation):
        super().__init__(test_method_name, fixture_store, fixture_namespace, variation)

        slash.logger.info("Initializing Chrome Driver")
        self.driver = webdriver.Chrome()
        slash.logger.info("Successfully initialized Chrome")
        self.driver.maximize_window()
        slash.logger.info("Chrome Maximized")

    def before(self):
        super().before()

    def after(self):
        super().after()