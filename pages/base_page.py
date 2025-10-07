import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимость элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельность элемента")
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_clickable_element(locator, timeout)
        element.click()

    @allure.step('Проверить, что элемент в viewport')
    def element_in_viewport(self, element):
        return self.driver.execute_script("""
            var elem = arguments[0];
            var rect = elem.getBoundingClientRect();
            return (rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                    rect.right <= (window.innerWidth || document.documentElement.clientWidth));
                    """, element)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, timeout).until(lambda driver: self.element_in_viewport(element))

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Ввод текста в поле')
    def send_text_to_input(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст уведомления')
    def get_alert_notification(self):
        alert = Alert(self.driver)
        alert_notification = alert.text
        return alert_notification

    @allure.step('Закрыть уведомление')
    def close_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    @allure.step('Сравнение ОР с ФР')
    def assert_test(self, actual_result, expected_result):
        assert actual_result == expected_result