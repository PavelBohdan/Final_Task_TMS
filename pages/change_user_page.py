from pages.base_page import BasePage
from pages.change_user_page_locators import ChangeUserPageLocators
from tools.db_steps import db_get_test_user_id

"""Страница изменения данных пользователя"""


class ChangeUserPage(BasePage):
    id = db_get_test_user_id()
    # есть вопрос по этой ссылке с запросом id из базы данных. Необходимо ли так делать?
    URL = ('http://localhost:8000/admin/auth/user/{id}/change/')

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def add_permissions_for_user(self):
        add_permissions_checkbox = self.find_element(
            ChangeUserPageLocators.STAFF_STATUS_CHECKBOX)
        add_permissions_checkbox.click()
        save_button = self.find_element(
            ChangeUserPageLocators.SAVE_BUTTON)
        save_button.click()
