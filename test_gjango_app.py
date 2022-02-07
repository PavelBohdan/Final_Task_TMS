from pages.main_page import MainPage
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from tools import db_steps

"""Страница с тестами"""


def test_add_new_user(browser):
    """
    1.	Открыть приложение
    2.	Войти в админку
    3.	Создать пользователя
    """
    main_page = MainPage(browser)
    main_page.open()
    login_page = main_page.open_login_page()
    admin_page = login_page.input_admin_credentials()
    add_user = admin_page.new_user()
    new_user = add_user.add_new_user()
    save_new_user = new_user.add_permissions_for_user()

    """5.	Выйти из приложение"""
    admin_page = AdminPage(browser)
    admin_page.open()
    log_out_page = admin_page.log_out()

    """4.	Проверить что пользователь создан в дб"""
    assert 'test_user' in db_steps.db_users()
