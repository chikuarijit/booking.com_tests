import slash
import time
from . import utils
from . import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .booking_home import Home


class LanguagePage(Home):

    def launch(self):
        if not self.loaded:
            slash.logger.info("Launching Language Page")
            slash.logger.info("Clicking on Language Button")
            self.language_button.click()
            slash.logger.info("Language Page launched")
        else:
            slash.logger.info("Language Page already loaded")
        time.sleep(2)

    @property
    def loaded(self):
        try:
            return self.select_language_heading.text.\
                strip() == const.LANGUAGE_TEXT
        except:
            return False

    @property
    def select_language_heading(self):
        element = utils.get_wait(self.driver).until(
            EC.visibility_of_element_located
            ((By.XPATH, const.SELECT_LANGUAGE_HEADING_LOCATOR)))

        return element

    def select_language(self, language_code):
        """
        Selects Language
        :param language_code: "English (US)"
        :returns
        """
        if not self.loaded:
            self.launch()
        # Wait for all language elements to be visible
        language_list = utils.get_wait(self.driver).until(
            EC.visibility_of_all_elements_located(utils.language_lists_locator())
        )

        # Loop through the buttons and find the desired language
        for language in language_list:
            # Get the inner div containing the currency code
            if language.text == language_code:
                language.click()
                slash.logger.info(f"Selected {language} Language")
                return True

        raise Exception(f"Language '{language_code}' not found.")