from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators
from pages.admin_page import AdminPage
from pages.change_user_page import ChangeUserPage
from constants import ADMIN_USERNAME, ADMIN_PASSWORD, NEW_USER_USERNAME, NEW_USER_PASSWORD

"""Страница Логина"""


class LoginPage(BasePage):
    URL = 'http://localhost:8000/admin/login/?next=/admin/'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def input_admin_credentials(self):
        '''Функция вводит логин и пароль'''
        username_field = self.find_element(LoginPageLocators.USERNAME)
        username_field.send_keys(ADMIN_USERNAME)
        password_field = self.find_element(LoginPageLocators.PASSWORD)
        password_field.send_keys(ADMIN_PASSWORD)
        login_in_button = self.find_element(LoginPageLocators.LOGIN_IN_BUTTON)
        login_in_button.click()
        return AdminPage(self.browser)

    def user_already_exist(self):
        error_message = self.find_elements(
            LoginPageLocators.USERNAME_ALREADY_EXISTS)
        if error_message != None:
            return True
        else:
            return False

    def input_user_credentials(self):
        '''Функция вводит логин и пароль нового пользователя'''
        username_field = self.find_element(LoginPageLocators.USERNAME)
        username_field.send_keys(NEW_USER_USERNAME)
        password_field = self.find_element(LoginPageLocators.PASSWORD)
        password_field.send_keys(NEW_USER_PASSWORD)
        login_in_button = self.find_element(LoginPageLocators.LOGIN_IN_BUTTON)
        login_in_button.click()
        return AdminPage(self.browser)