import allure
from pages.base_page import BasePage
from pages.base_locators import Locators


class Notifications(BasePage):

    @allure.step("Проверить заголовок уведомления")
    def check_notification(self, link_text: str):
        return self.check_text_element(Locators.NOTIFY_TITLE).text == link_text

    @allure.step("Закрыть и очистить уведомления")
    def clear_and_close_notification(self):
        self._click(Locators.NOTIFY_CLEAR_CLOSE)
