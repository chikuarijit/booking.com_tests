import slash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

class BookingBaseTest(slash.Test):
    def __init__(self, test_method_name, fixture_store, fixture_namespace, variation):
        super().__init__(test_method_name, fixture_store, fixture_namespace, variation)
        self.driver = self.init_driver()

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")  # Enable if needed
        chrome_options.add_argument("--disable-gpu")
        slash.logger.info("Initializing Chrome Driver")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        slash.logger.info("Chrome initialized and maximized")
        return driver

    def before(self):
        super().before()

    def after(self):
        super().after()
        try:
            if not slash.context.result.is_success():
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                log_dir = slash.context.result.get_log_dir()
                os.makedirs(log_dir, exist_ok=True)
                screenshot_path = os.path.join(log_dir, f"failure_image_{timestamp}.png")
                self.driver.save_screenshot(screenshot_path)
                slash.logger.info(f"Saved failure screenshot: {screenshot_path}")
        finally:
            self.driver.quit()
            slash.logger.info("Chrome driver quit successfully")
