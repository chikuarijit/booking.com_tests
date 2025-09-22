import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from my_ui_booking.activities.booking_home import Home
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By


class TestHome(unittest.TestCase):

    def setUp(self):
        # Mock the WebDriver
        self.mock_driver = MagicMock()
        self.home = Home(self.mock_driver)

    @patch(
        "my_ui_booking.activities.booking_home.Home.booking_logo",
        new_callable=PropertyMock,
    )
    def test_is_booking_logo_displayed_true(self, mock_booking_logo):
        # Mock the WebElement returned by booking_logo
        mock_element = MagicMock()
        mock_element.is_displayed.return_value = True
        mock_booking_logo.return_value = mock_element

        self.assertTrue(self.home.is_booking_logo_displayed)

    @patch(
        "my_ui_booking.activities.booking_home.Home.booking_logo",
        new_callable=PropertyMock,
    )
    def test_is_booking_logo_displayed_false(self, mock_booking_logo):
        # Mock the WebElement returned by booking_logo
        mock_element = MagicMock()
        mock_element.is_displayed.return_value = False
        mock_booking_logo.return_value = mock_element

        self.assertFalse(self.home.is_booking_logo_displayed)


if __name__ == "__main__":
    unittest.main()
