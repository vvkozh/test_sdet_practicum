import allure
import helpers
from pages.base_page import BasePage
from data import DataFormField
from locators.form_fields_locator import Fields

class FormFieldsPage(BasePage):
    @allure.step('Заполнить имя')
    def send_name(self):
        self.send_text_to_input(Fields.FIELD_NAME, DataFormField.NAME)

    @allure.step('Заполнить пароль')
    def send_password(self):
        self.scroll_to_element(Fields.FIELD_PASSWORD)
        self.send_text_to_input(Fields.FIELD_PASSWORD, DataFormField.PASSWORD)

    @allure.step('Выбрать любимый напиток')
    def choosing_favorite_drink(self):
        for drink in DataFormField.FAVORITE_DRINK:
            self.scroll_to_element(Fields.locator_favorite_drink(drink))
            self.click_on_element(Fields.locator_favorite_drink(drink))

    @allure.step('Выбрать любимый цвет')
    def choosing_favorite_color(self):
        self.scroll_to_element(Fields.locator_favorite_color(DataFormField.FAVORITE_COLOR))
        self.click_on_element(Fields.locator_favorite_color(DataFormField.FAVORITE_COLOR))

    @allure.step('Выбор опции "Do you like automation?"')
    def choosing_like_auto(self):
        self.scroll_to_element(Fields.locator_like_auto(DataFormField.LIKE_AUTO))
        self.click_on_element(Fields.locator_like_auto(DataFormField.LIKE_AUTO))

    @allure.step('Получить списка инструментов')
    def get_auto_tools(self):
        self.scroll_to_element(Fields.AUTO_TOOLS)
        tools = self.get_text_on_element(Fields.AUTO_TOOLS)
        return tools

    @allure.step('Заполнить поле Email')
    def send_email(self):
        self.scroll_to_element(Fields.FIELD_EMAIL)
        self.send_text_to_input(Fields.FIELD_EMAIL, DataFormField.EMAIL)

    @allure.step('Заполнить сообщение')
    def send_message(self, tools):
        number_of_tools = helpers.count_tolls(tools)
        largest_tool = helpers.choose_largest_tool(tools)
        message = (f'Количество инструментов - {number_of_tools}.\n'
                   f'Наибольшее количество символов в инструменте - {largest_tool}.')
        self.scroll_to_element(Fields.FIELD_MESSAGE)
        self.send_text_to_input(Fields.FIELD_MESSAGE, message)

    @allure.step('Клик на кнопку Submit')
    def click_submit(self):
        self.scroll_to_element(Fields.BUT_SUBMIT)
        self.click_on_element(Fields.BUT_SUBMIT)

    @allure.step('Получить текст уведомления')
    def get_alert_text(self):
        text_alert = self.get_alert_notification()
        self.close_alert()
        return text_alert

    @allure.step('Сравнить ОР с ФР')
    def assert_alert(self, actual_text_alert):
        self.assert_test(actual_text_alert, DataFormField.EXPECTED_TEXT_ALERT)