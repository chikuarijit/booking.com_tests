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
            return self.select_currency_heading.text.strip() == const.CURRENCY_TEXT
        except:
            return False

    @property
    def select_currency_heading(self):
        element = utils.get_wait(self.driver).until(
            EC.visibility_of_element_located(
                (By.XPATH, const.SELECT_CURRENCY_HEADING_LOCATOR)
            )
        )

        return element

    def get_all_currencies(self):
        if not self.loaded:
            self.launch()
        # Wait for all currency buttons to be visible
        currencies_list = utils.get_wait(self.driver).until(
            EC.visibility_of_all_elements_located(utils.currency_lists_locator())
        )

        return currencies_list

    def get_selected_currency(self):
        currency_list = self.get_all_currencies()
        for currency in currency_list:
            if currency.get_attribute("aria-current") == "true":
                curr = currency.text
                self.close_button.click()

                return curr

        raise Exception(f"No selected language found")

    def is_currency_selected(self, currency):
        return currency in self.get_selected_currency()

    def select_currency(self, currency_code):
        """
        Select a currency by its code, e.g., 'INR', 'USD', 'EUR'.
        """
        currency_list = self.get_all_currencies()

        # Loop through the buttons and find the desired currency
        for currency in currency_list:
            # Get the inner div containing the currency code
            currency_div = currency.find_element(
                By.CSS_SELECTOR, "div.CurrencyPicker_currency"
            )
            if currency_div.text.strip() == currency_code:
                currency.click()
                return True  # Successfully clicked

        raise Exception(f"Currency '{currency_code}' not found.")

    @property
    def close_button(self):
        button = utils.get_wait(self.driver).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, const.CLOSE_BUTTON))
        )

        return button
