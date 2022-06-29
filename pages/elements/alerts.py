import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.base_locators import Locators


class Alerts(BasePage):
    CLOSE_ICON = (By.CSS_SELECTOR, ".ant-modal-close-x")
    CHOOSE_ALL = (By.CSS_SELECTOR, ".bid__link .link-text")
    CANCEL = (By.XPATH, "//span[text()=' Отмена ']")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    @allure.step("Нажать 'Закрыть' в модальном окне")
    def close_alert(self):
        time.sleep(7)
        self._click(self.CLOSE_ICON)

    @allure.step("Нажать 'Отменить' в модальном окне")
    def cancel_alert(self):
        self._click(self.CANCEL)

    @allure.step("Нажать 'Подтвердить' в модальном окне")
    def confirm_alert(self):
        self._click(Locators.CONTINUE)

    @allure.step("Активировать чекбокс")
    def set_checkbox(self, order):
        checkbox = self._find_elements(self.CHECKBOX)[order]
        if checkbox.get_attribute('checked') == None or checkbox.get_attribute('checked') == "false":
            checkbox.click()
        else:
            self.allure_attach()
            raise AssertionError(f"Чекбокс {order + 1} активен")

    @allure.step("Деактивировать чекбокс")
    def unset_checkbox(self, order):
        checkbox = self._find_elements(self.CHECKBOX)[order]
        if checkbox.get_attribute('checked') == "true":
            self.browser.execute_script("arguments[0].click();", checkbox)
        else:
            self.allure_attach()
            raise AssertionError(f"Чекбокс {order + 1} неактивен")

    @allure.step("Отменить все категории подписки")
    def cancel_all_categories(self):
        self._find_elements(self.CHOOSE_ALL)[1].click()

    @allure.step("Выбрать все категории подписки")
    def choose_all_categories(self):
        self._find_elements(self.CHOOSE_ALL)[0].click()
