from pages.base_page import BasePage
from pages.add_user_page_locators import AddUserPageLocators
from pages.change_user_page import ChangeUserPage

"""Страница создания пользователя"""


class AddUserPage(BasePage):
    URL = 'http://localhost:8000/admin/auth/user/add/'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def add_new_user(self):
        new_username = self.find_element(
            AddUserPageLocators.NEW_USERNAME_LOCATOR)
        new_username.send_keys('test_user')
        new_password = self.find_element(
            AddUserPageLocators.NEW_PASSWORD_LOCATOR)
        new_password.send_keys('12Test3456')
        new_password_confirmation = self.find_element(
            AddUserPageLocators.NEW_PASSWORD_CONFIRMATION_LOCATOR)
        new_password_confirmation.send_keys('12Test3456')
        save_button = self.find_element(
            AddUserPageLocators.SAVE_BUTTON_LOCATOR)
        save_button.click()
        return ChangeUserPage(self.browser)
