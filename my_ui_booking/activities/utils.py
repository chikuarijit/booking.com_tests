from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import constants


def get_wait(driver):
    return WebDriverWait(driver, constants.WAIT_TIMEOUT)