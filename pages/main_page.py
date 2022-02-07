from pages.base_page import BasePage
from pages.main_page_locators import MainPageLocators
from pages.login_page import LoginPage

"""Начальная страница"""


class MainPage(BasePage):
    URL = 'http://localhost:8000'

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def open_login_page(self):
        '''Функция  открывает и возвращает страницу админа'''
        admin_page_link = self.find_element(
            MainPageLocators.GO_TO_ADMIN_BUTTON_LOCATOR)
        admin_page_link.click()
        return LoginPage(self.browser)
