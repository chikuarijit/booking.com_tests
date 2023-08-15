import slash
from . import constants as const
from . import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support import \
    expected_conditions as EC
import time


class Occupancy:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):
        slash.logger.info("Launching Occupancy")
        button_element = (self.driver.find_element
                          (By.CSS_SELECTOR,
                           '[data-testid="occupancy-config"]'))
        button_element.click()
        slash.logger.info("Successcully launched Occupancy")

    def adults(self, number):
        container_element = self.driver.find_element(By.CLASS_NAME, "bfb38641b0")
        slash.logger.info("Resetting adults number to 1")
        while True:
            if utils.numbers(self.driver, container_element) == 1:
                break
            utils.decrease_button(self.driver, container_element).click()
        slash.logger.info("Adults number reseted to 1")

        slash.logger.info(f"Setting adults number to {number}")
        for _ in range(number - 1):
            utils.increase_button(self.driver, container_element).click()
        slash.logger.info(f"Adult number successfully set to {number}")

    @property
    def adults_number(self):
        container_element = self.driver.find_element(By.CLASS_NAME, "bfb38641b0")
        return utils.numbers(self.driver, container_element)

    def children(self):
        children_container_element = self.driver.find_element(By.CLASS_NAME,
                                                              "bfb38641b0")  # Container element for children tab
        children_increase_button = children_container_element.find_element(By.CSS_SELECTOR,
                                                                           "button.children-increase-button")  # Increase button within children tab
        children_increase_button.click()

    def rooms(self):
        parent_container_element = self.driver.find_element(By.CLASS_NAME, "a7a72174b8")

        # Find the increase button element within the parent container
        increase_button = parent_container_element.find_element(By.CSS_SELECTOR, "button.f4d78af12a")

        # Click the increase button
        increase_button.click()
        increase_button.click()


