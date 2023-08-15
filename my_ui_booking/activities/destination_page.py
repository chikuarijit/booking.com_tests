import slash
import time
from . import utils
from . import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DestinationPage:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):