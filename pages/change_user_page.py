from pages.base_page import BasePage
from pages.change_user_page_locators import ChangeUserPageLocators

"""Страница изменения данных пользователя"""


class ChangeUserPage(BasePage):
    URL = ('http://localhost:8000/admin/auth/user/change/')

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def add_permissions_for_user(self):
        add_permissions_checkbox = self.find_element(
            ChangeUserPageLocators.STAFF_STATUS_CHECKBOX)
        add_permissions_checkbox.click()
        save_button = self.find_element(
            ChangeUserPageLocators.SAVE_BUTTON)
        save_button.click()
