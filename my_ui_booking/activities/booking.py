import slash
from selenium.common import TimeoutException
from . import constants as const
from . import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support import \
    expected_conditions as EC


class Booking:
    def __init__(self, driver):
        self.driver = driver

    def open_landing_page(self):
        slash.logger.info(f"Opening {const.BASE_URL}")
        self.driver.get(const.BASE_URL)
        slash.logger.info(f"{const.BASE_URL} successfully opened")
        try:
            self.handle_popup()
        except TimeoutException:
            slash.logger.info("No popup detected")

    def handle_popup(self):
        slash.logger.info("Closing Popup")
        button = utils.get_wait(self.driver).until(
            EC.element_to_be_clickable
            ((By.CSS_SELECTOR, const.CLOSE_POPUP)))
        button.click()
        slash.logger.info("Popup Closed")

    def enter_destination(self, place_name):
        try:
            button = utils.get_wait(self.driver).until(
                EC.element_to_be_clickable
                ((By.CSS_SELECTOR, 'div.eac0b6e5ba span[data-testid="input-clear"]')))

            button.click()
        except:
            pass

        slash.logger.info("Finding Search Field")
        search_field = self.driver.find_element(By.ID, ":re:")
        slash.logger.info("Clicking on Search Filed")
        search_field.click()
        slash.logger.info("Successfully clicked on Search Field")
        search_field.send_keys(place_name)
        slash.logger.info(f"Entered text {place_name}")
        (utils.click_element_with_text
         (self.driver, place_name=place_name))

    def dates_loaded(self):
        try:
            utils.get_wait(self.driver).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, 'button[aria-controls="calendar-searchboxdatepicker"] span.a53cbfa6de'),
                    "Calendar") and
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, 'button[aria-controls="flexible-searchboxdatepicker"] span.a53cbfa6de'),
                    "I'm flexible")
            )
            return True
        except:
            return False

    def select_checkin_checkout_dates(self, checkin_date, checkout_date):
        if not self.dates_loaded():
            button = utils.get_wait(self.driver).until(
                EC.element_to_be_clickable
                ((By.CSS_SELECTOR,
                  'button[data-testid="date-display-field-start"]')))
            button.click()

        utils.select_date(self.driver, checkin_date)
        utils.select_date(self.driver, checkout_date)

