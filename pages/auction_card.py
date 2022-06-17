import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Auction(BasePage):
    FAVORITE_AUCTION = (By.CSS_SELECTOR, ".add-to-favorite")

    @allure.step("Добавить аукцион в избранное из карточки процедуры")
    def set_favorites_from_card(self):
        return self._click(self.FAVORITE_AUCTION)
