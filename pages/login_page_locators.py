from selenium.webdriver.common.by import By

'''Локаторы на странице логина'''


class LoginPageLocators:
    USERNAME = (
        By.XPATH, '//input[@id="id_username"]')
    PASSWORD = (
        By.XPATH, '//input[@id="id_password"]')
    LOGIN_IN_BUTTON = (
        By.XPATH, '//input[@value="Log in"]')
    USERNAME_ALREADY_EXISTS = (
        By.XPATH, '//ul[@class="errorlist"]')
