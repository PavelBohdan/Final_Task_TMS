from selenium.webdriver.common.by import By

"""Локаторы на странице изменения данных пользователя"""


class ChangeUserPageLocators:

    STAFF_STATUS_CHECKBOX = (
        By.XPATH, '//input[@id="id_is_staff"]')
    SAVE_BUTTON = (
        By.XPATH, '//input[@value="Save"]')
