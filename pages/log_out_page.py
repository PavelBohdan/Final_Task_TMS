from pages.base_page import BasePage
from pages.log_out_page_locators import LogOutPageLocators

"""Страница LogOut"""


class LogOutPage(BasePage):
    URL = 'http://localhost:8000/admin/logout/'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def login_again(self):
        login_again_button = self.find_element(
            LogOutPageLocators.LOGIN_AGAIN_LOCATOR)
        login_again_button.click()
