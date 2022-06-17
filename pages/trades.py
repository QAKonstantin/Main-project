import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.elements.header import Header
from pages.base_locators import Locators


class Trades(BasePage):
    FAVORITE = (By.CSS_SELECTOR, ".favorite .icon")
    ACTIVE_FAVORITE = (By.CSS_SELECTOR, ".favorite__selected .icon")
    FAVORITES = (By.CSS_SELECTOR, ".ant-switch")
    MATERIAL_NAME = (By.CSS_SELECTOR, ".auction-table-name .material-name")
    GET_ACCREDITATION = (By.CSS_SELECTOR, ".accreditation-btn")

    @allure.step("Добавить в избранное")
    def set_favorites(self):
        mas = self._find_elements(self.ACTIVE_FAVORITE)
        if (len(mas) > 0):
            for i in range(len(mas)):
                mas[i].click()
        return self._find_elements(self.FAVORITE)[0].click()

    @allure.step("Удалить из избранного")
    def unset_favorites(self):
        self.browser.refresh()
        mas = self._find_elements(self.ACTIVE_FAVORITE)
        if (len(mas) > 0):
            for i in range(len(mas)):
                mas[i].click()

    @allure.step("Перейти к избранному")
    def setter_favorites_filter(self):
        Header(self.browser)._move_to_dropdown()
        self.actions.click(self._find_element(self.FAVORITES)).perform()

    @allure.step("Перейти в карточку процедуры")
    def move_to_auction_card(self, i):
        return self._find_elements(self.MATERIAL_NAME)[i].click()

    @allure.step("Сменить отображение аукционов на Подробно")
    def change_table_display_to_detailed(self):
        time.sleep(3)
        self._click(Locators.DISPLAY_TABLE_SHORT)
        self._click(Locators.DISPLAY_TABLE_DETAILED)

    @allure.step("Сменить отображение аукционов на Кратко")
    def change_table_display_to_short(self):
        self._click(Locators.DISPLAY_TABLE_DETAILED)
        self._click(Locators.DISPLAY_TABLE_SHORT)

    def get_accreditation(self):
        self.submit(self.GET_ACCREDITATION)
