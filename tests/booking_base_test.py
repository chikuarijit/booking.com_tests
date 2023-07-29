import slash as slash
from selenium import webdriver


class BookingBaseTest(slash.Test):
    def __init__(self, test_method_name, fixture_store, fixture_namespace, variation):
        super().__init__(test_method_name, fixture_store, fixture_namespace, variation)

    def before(self):
        super().before()
        slash.logger.info("Opening Chrome")
        self.driver = webdriver.Chrome()
        slash.logger.info("Chrome Opened")
        self.driver.maximize_window()
        slash.logger.info("Chrome Maximized")

    def after(self):
        slash.logger.info("Closing Browser")
        self.driver.quit()
        slash.logger.info("Completed test")

    def _get_session_id(self):
        return self.session.id if hasattr(self, "session") else None

    def _get_test_metadata_id(self):
        return self.test_metadata.id if hasattr(self, "test_metadata") else None



