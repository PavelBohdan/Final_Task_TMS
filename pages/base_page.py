from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Базовая страница"""


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        return self.browser.get(self.url)

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            return None

    def find_elements(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located(locator))
            return element
        except TimeoutException:
            return None
