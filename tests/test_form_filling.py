from pages.form_fields_page import FormFieldsPage

class TestFormFilling:
    def test_form_filling(self, driver):
        # arrange
        form_filling = FormFieldsPage(driver)

        # act
        form_filling.send_name()
        form_filling.send_password()
        form_filling.choosing_favorite_drink()
        form_filling.choosing_favorite_color()
        form_filling.choosing_like_auto()
        tools = form_filling.get_auto_tools()
        form_filling.send_email()
        form_filling.send_message(tools)
        form_filling.click_submit()
        alert_text = form_filling.get_alert_text()

        # assert
        form_filling.assert_alert(alert_text)
