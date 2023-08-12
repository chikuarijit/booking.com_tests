import slash
from slash_step import STEP
from .booking_base_test import BookingBaseTest
from my_ui_booking import booking, \
    change_currency, change_language


class LandingPage(BookingBaseTest):
    def before(self):
        super().before()
        self.booking_instance = booking.\
            Booking(self.driver)
        self.currency_changer = change_currency.\
            ChangeCurrency(self.driver)
        self.language_changer = change_language.\
            ChangeLanguage(self.driver)

    @slash.tag("First")
    def test_opening_landing_page(self):

        with STEP("Step 1 : Preconditions: "
                  "Open Booking.com home page"):
            self.booking_instance.open_landing_page()
            self.booking_instance.handle_popup()

        with STEP("Step 2: Open currency page"):
            self.currency_changer.launch()
            assert self.currency_changer.loaded, \
                "Currency page not loaded"
            self.currency_changer.select_currency("USD")

        with STEP("Step 3: Open Language Page"):
            self.language_changer.launch()
            assert self.language_changer.loaded, \
                "Language page not loaded"
            self.language_changer.\
                select_language("English (US)")
