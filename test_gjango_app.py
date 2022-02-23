from pages.main_page import MainPage
from pages.admin_page import AdminPage
from constants import NEW_USER_USERNAME, NEW_USER_PASSWORD
from tools.db_steps import DataBase
import pytest
import allure

"""Страница с тестами"""


@allure.story('Add new user')
@pytest.mark.parametrize('login, password', [(NEW_USER_USERNAME, NEW_USER_PASSWORD)])
def test_add_new_user(browser, postgres_connections, login, password):
    """
    1.	Открыть приложение
    2.	Войти в админку
    3.	Создать пользователя
    """
    with allure.step('Open main page'):
        main_page = MainPage(browser)
        main_page.open()
    with allure.step('Open admin page'):
        login_page = main_page.open_login_page()
        admin_page = login_page.input_admin_credentials()
    with allure.step('Add new user'):
        add_user = admin_page.new_user()
        new_user = add_user.add_new_user(login, password)
        save_new_user = new_user.add_permissions_for_user()

    """5.	Выйти из приложения"""
    with allure.step('Logout from app'):
        admin_page = AdminPage(browser)
        admin_page.open()
        log_out_page = admin_page.log_out()

    """4.	Проверить что пользователь создан в дб"""
    with allure.step('Check new user in database'):
        postgres = DataBase(postgres_connections)
        assert NEW_USER_USERNAME in postgres.db_users()


@allure.story('Open app by new user')
def test_open_app_by_new_user(browser):
    """
    6. Bойти как созданный пользователь
    7. Проверить, что приложение открылось
    """
    with allure.step('Open main page'):
        main_page = MainPage(browser)
        main_page.open()
    with allure.step('Login by new user'):
        login_page = main_page.open_login_page()
        admin_page = login_page.input_user_credentials()
        welcome_user_element = admin_page.find_welcome_user_element()
    with allure.step('Check that user is logged in'):
        assert welcome_user_element.text == NEW_USER_USERNAME.upper()
