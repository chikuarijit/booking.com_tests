import slash
from slash_step import STEP
from .booking_base_test import BookingBaseTest


class LandingPage(BookingBaseTest):

    def before(self):
        super().before()

    @slash.tag("First")
    def test_opening_landing_page(self):

        with STEP("Step 1: Open Booking.com home page"):
            self.booking_home.launch()

            assert self.booking_home.loaded, "Landing page not loaded"

        with STEP("Step 2: Open Currency Page"):
            self.currency_page.launch()

            assert self.currency_page.loaded, "Currency page not loaded"

        with STEP("Step 3: Change currency to USD"):
            currency_list = self.currency_page.get_all_currencies()
            assert len(currency_list), "Currency List is empty"
            assert any(
                "USD" in currency.text for currency in currency_list
            ), "USD is not in currency list"

            self.currency_page.select_currency("USD")

        with STEP("Step 4: USD currency is selected"):
            assert self.currency_page.is_currency_selected("USD"), "USD is not selected"

        with STEP("Step 5: Open Language Page"):
            self.language_page.launch()
            assert self.language_page.loaded, "Language page not loaded"

        with STEP("Step 6: Change language to English (US)"):
            language_list = self.language_page.get_all_languages()
            assert len(language_list), "Language List is empty"
            assert any(
                "English (US)" in language.text for language in language_list
            ), "English (US) is not in language list"

            self.language_page.select_language("English (US)")

        with STEP("Step 7: Verify English (US) language is selected"):
            assert self.language_page.is_language_selected(
                "English (US)"
            ), "English (US) is not selected"

        # with STEP("Step 4: Enter destination Kolkata"):
        #     self.booking_instance.enter_destination("Kolkata")
        #
        # with STEP("Step 5: Select check-in and check-out dates"):
        #     self.booking_instance.select_checkin_checkout_dates("17", "19")
        #
        # with STEP("Step 6: Set occupancy to 25 adults"):
        #     self.occupancy_instance.launch()
        #     self.occupancy_instance.adults(25)
        #     assert self.occupancy_instance.adults_number == 25, "Adults number is not set to 25"
        #
        # with STEP("Step 7: Open Search page"):
        #     self.search_instance.launch()
        #     assert self.search_instance.loaded(), "Search page not loaded"
