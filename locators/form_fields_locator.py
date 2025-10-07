from selenium.webdriver.common.by import By

class Fields:
    FIELD_NAME = (By.ID, 'name-input')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '[type="password"]')
    AUTO_TOOLS = (By.XPATH, '//label[text()="Automation tools"]/following-sibling::ul')
    FIELD_EMAIL = (By.ID, 'email')
    FIELD_MESSAGE = (By.NAME, 'message')
    BUT_SUBMIT = (By.ID, 'submit-btn')

    @staticmethod
    def locator_favorite_drink(drink):
        return By.XPATH, f'//input[@value="{drink}"]'

    @staticmethod
    def locator_favorite_color(color):
        return By.XPATH, f'//input[@value="{color}"]'

    @staticmethod
    def locator_like_auto(like_auto):
        return By.XPATH, f'//option[@value="{like_auto}"]'

