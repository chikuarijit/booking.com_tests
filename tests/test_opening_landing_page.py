import slash
from slash_step import STEP
from .booking_base_test import BookingBaseTest
from ..my_ui_booking.activities import booking, change_currency, change_language, occupancy, search

class LandingPage(BookingBaseTest):

    def before(self):
        super().before()
        self.booking_instance = booking.Booking(self.driver)
        self.currency_changer = change_currency.ChangeCurrency(self.driver)
        self.language_changer = change_language.ChangeLanguage(self.driver)
        self.occupancy_instance = occupancy.Occupancy(self.driver)
        self.search_instance = search.Search(self.driver)

    @slash.tag("First")
    def test_opening_landing_page(self):

        with STEP("Open Booking.com home page"):
            self.booking_instance.open_landing_page()
            assert self.booking_instance.is_loaded(), "Landing page not loaded"

        with STEP("Change currency to USD"):
            self.currency_changer.launch()
            assert self.currency_changer.loaded(), "Currency page not loaded"
            self.currency_changer.select_currency("USD")

        with STEP("Change language to English (US)"):
            self.language_changer.launch()
            assert self.language_changer.loaded(), "Language page not loaded"
            self.language_changer.select_language("English (US)")

        with STEP("Enter destination Kolkata"):
            self.booking_instance.enter_destination("Kolkata")

        with STEP("Select check-in and check-out dates"):
            self.booking_instance.select_checkin_checkout_dates("17", "19")

        with STEP("Set occupancy to 25 adults"):
            self.occupancy_instance.launch()
            self.occupancy_instance.adults(25)
            assert self.occupancy_instance.adults_number == 25, "Adults number is not set to 25"

        with STEP("Open Search page"):
            self.search_instance.launch()
            assert self.search_instance.loaded(), "Search page not loaded"
