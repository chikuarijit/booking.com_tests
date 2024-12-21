import slash as slash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class BookingBaseTest(slash.Test):
    def __init__(self, test_method_name, fixture_store, fixture_namespace, variation):
        super().__init__(test_method_name, fixture_store, fixture_namespace, variation)

        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        slash.logger.info("Initializing Chrome Driver")
        self.driver = webdriver.Chrome( options=chrome_options)
        slash.logger.info("Successfully initialized Chrome")
        self.driver.maximize_window()
        slash.logger.info("Chrome Maximized")

    def before(self):
        super().before()

    def after(self):
        super().after()
        slash.logger.info("1111111111111111")
        if not slash.context.result.is_success():
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            self.driver.save_screenshot(slash.context.result.get_log_dir()+ f"/failure_image_{timestamp}.png")
