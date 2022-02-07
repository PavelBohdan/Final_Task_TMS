from selenium.webdriver.common.by import By

'''Локаторы на странице создания пользователя'''


class AddUserPageLocators:
    NEW_USERNAME_LOCATOR = (
        By.XPATH, '//input[@id="id_username"]')
    NEW_PASSWORD_LOCATOR = (
        By.XPATH, '//input[@id="id_password1"]')
    NEW_PASSWORD_CONFIRMATION_LOCATOR = (
        By.XPATH, '//input[@id="id_password2"]')
    SAVE_BUTTON_LOCATOR = (
        By.XPATH, '//input[@value="Save"]')
