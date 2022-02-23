from pages.base_page import BasePage
from pages.admin_page_locators import AdminPageLocators
from pages.add_user_page import AddUserPage
from pages.log_out_page import LogOutPage

"""Страница админки"""


class AdminPage(BasePage):
    URL = 'http://localhost:8000/admin/'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def new_user(self):
        new_user_button = self.find_element(
            AdminPageLocators.ADD_NEW_USER_LOCATOR)
        new_user_button.click()
        return AddUserPage(self.browser)

    def log_out(self):
        log_out_button = self.find_element(
            AdminPageLocators.LOG_OUT_LINK_LOCATOR)
        log_out_button.click()
        return LogOutPage(self.browser)

    def find_welcome_user_element(self):
        welcome_user_element = self.find_element(AdminPageLocators.WELCOME_USER_ELEMENT_LOCATOR)
        return welcome_user_element
