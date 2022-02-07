from selenium.webdriver.common.by import By

'''Локаторы на начальной странице'''


class MainPageLocators:
    GO_TO_ADMIN_BUTTON_LOCATOR = (
        By.XPATH, '//a[@class="btn btn-primary my-2"]')
        
