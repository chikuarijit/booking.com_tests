import slash
from slash_step import STEP
from .booking_base_test import BookingBaseTest
from my_ui_booking import booking
from my_ui_booking import change_currency


class LandingPage(BookingBaseTest):
    def before(self):
        super().before()
        self.booking_instance = booking.Booking(self.driver)
        self.currency_changer = change_currency.ChangeCurrency(self.driver)

    @slash.tag("First")
    def test_opening_landing_page(self):

        with STEP("Step 1 : Preconditions: Open Booking.com home page"):
            self.booking_instance.open_landing_page()
            self.booking_instance.handle_popup()

        with STEP("Step 2: Open currency page"):
            self.currency_changer.launch()
            assert self.currency_changer.loaded, \
                "Currency page not loaded"


            

