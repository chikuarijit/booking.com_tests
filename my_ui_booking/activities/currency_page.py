import slash
import time
from . import utils
from . import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .booking_home import Home


class CurrencyPage(Home):

    def launch(self):
        if not self.loaded:
            slash.logger.info("Launching Currency Page")
            slash.logger.info("Clicking on Currency Button")
            self.currency_button.click()
            slash.logger.info("Currency Page launched")
        else:
            slash.logger.info("Currency Page already loaded")
        time.sleep(2)

    @property
    def loaded(self):
        try:
            return self.select_currency_heading.text.\
                strip() == const.CURRENCY_TEXT
        except:
            return False

    @property
    def select_currency_heading(self):
        element = utils.get_wait(self.driver).until(
            EC.visibility_of_element_located
            ((By.XPATH, const.SELECT_CURRENCY_HEADING_LOCATOR)))

        return element

    def select_currency(self, currency_code):
        """
        Select a currency by its code, e.g., 'INR', 'USD', 'EUR'.
        """
        if not self.loaded:
            self.launch()
        # Wait for all currency buttons to be visible
        buttons = utils.get_wait(self.driver).until(
            EC.visibility_of_all_elements_located(utils.currency_lists_locator())
        )

        # Loop through the buttons and find the desired currency
        for button in buttons:
            # Get the inner div containing the currency code
            currency_div = button.find_element(By.CSS_SELECTOR, "div.CurrencyPicker_currency")
            if currency_div.text.strip() == currency_code:
                button.click()
                return True  # Successfully clicked

        raise Exception(f"Currency '{currency_code}' not found.")
