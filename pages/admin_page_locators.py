from selenium.webdriver.common.by import By

'''Локаторы на странице админки'''


class AdminPageLocators:
    ADD_NEW_USER_LOCATOR = (
        By.XPATH, '//a[@href="/admin/auth/user/add/"]')
    LOG_OUT_LINK_LOCATOR = (
        By.XPATH, '//a[@href="/admin/logout/"]')
    WELCOME_USER_ELEMENT_LOCATOR = (
        By.XPATH, '//div[@id="user-tools"]//strong')
