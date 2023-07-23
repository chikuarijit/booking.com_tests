import slash
from slash_step import STEP
from .booking_base_test import BookingBaseTest


class LandingPage(BookingBaseTest):
    def before(self):
        super().before()

    @slash.tag("First")
    def test_opening_landing_page(self):

        with STEP("Step 1 : Preconditions"):
            self.open_landing_page()

