from selenium.webdriver.support.ui import WebDriverWait
from . import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import slash



def get_wait(driver):
    return WebDriverWait(driver, constants.WAIT_TIMEOUT)

def click_element_with_text(driver,place_name):
    element = (get_wait(driver).
               until(EC.element_to_be_clickable
                                    ((By.XPATH, f'//div[text()="{place_name}"]'))))
    element.click()
    slash.logger.info(f"Successfully Clicked on {place_name}")

def select_date(driver, date):
    date_element = (driver.find_element
                    (By.XPATH,
                     f'//span[text()="{date}"]'))
    date_element.click()
    slash.logger.info(f"Successfully Clicked on {date}")

def increase_button(driver,container_element):
    increase_button = container_element.find_element(By.CLASS_NAME, "f4d78af12a")
    return increase_button

def decrease_button(driver, container_element):
    decrease_button = container_element.find_element(By.CLASS_NAME, "e91c91fa93")
    return decrease_button

def numbers(driver, container_element):
    number_element = container_element.find_element(By.CLASS_NAME, "d723d73d5f")
    return int(number_element.text)