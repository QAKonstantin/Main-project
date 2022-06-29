import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    TRADES = (By.XPATH, "//a[text()=' Товары с уценкой ']")
    CATALOG = (By.XPATH, "//a[text()=' Каталог ']")
    ORDERS = (By.XPATH, "//a[text()=' Заказы ']")
    MY_ORDERS = (By.XPATH, "//a[text()=' Мои заказы ']")
    HELP = (By.XPATH, "//a[text()=' Помощь ']")
    SALE = (By.XPATH, "//a[text()=' Продажа ']")
    KEBAB = (By.CSS_SELECTOR, "use[*|href='/assets/images/sprite.svg#kebab']")
    CONTRAGENTS = (By.XPATH, "//a[text()=' Контрагенты ']")
    CONTRACTS = (By.XPATH, "//a[text()=' Договоры ']")
    USERS = (By.XPATH, "//a[text()=' Пользователи ']")
    MARKETPLACE = (By.XPATH, "//a[text()=' Маркетплейс ']")
    USER_INFO = (By.CSS_SELECTOR, ".auth-sso .auth")
    SUBSCRIPTION_MANAGE = (By.XPATH, "//div[text()=' Управление подписками ']")
    HEADER = (By.CSS_SELECTOR, ".layout-header__main")

    @allure.step("Перейти в Торги")
    def move_to_auctions(self):
        self._click(self.TRADES)
        time.sleep(7)

    @allure.step("Нажать на управление подписками")
    def open_subscription_management(self):
        self._move_to_dropdown()
        self.actions.pause(2).click(self._find_element(self.SUBSCRIPTION_MANAGE)).perform()
        time.sleep(2)

    @allure.step("Перейти в Каталог")
    def move_to_catalog(self):
        self.actions.pause(1).click(self._find_element(self.CATALOG)).perform()

    @allure.step("Перейти в Помощь")
    def move_to_help(self):
        self.actions.pause(1).click(self._find_element(self.HELP)).perform()

    @allure.step("Перейти в Заказы под БО")
    def move_to_orders_by_bo(self):
        self.actions.pause(1).click(self._find_element(self.ORDERS)).perform()

    @allure.step("Перейти в Мои заказы под покупателем")
    def move_to_orders_by_user(self):
        self.actions.pause(1).click(self._find_element(self.MY_ORDERS)).perform()

    @allure.step("Перейти на страницу Продажа")
    def move_to_sale(self):
        self._click(self.SALE)

    @allure.step("Перейти на страницу Контрагенты")
    def move_to_contragents(self):
        self._move_to_kebab()
        self._click(self.CONTRAGENTS)
        self._reset_cursor()

    @allure.step("Перейти на страницу Договоры")
    def move_to_contracts(self):
        self._move_to_kebab()
        self._click(self.CONTRACTS)
        self._reset_cursor()

    @allure.step("Перейти на страницу Пользователи")
    def move_to_users(self):
        self._move_to_kebab()
        self._click(self.USERS)
        self._reset_cursor()

    @allure.step("Перейти в Маркетплейс")
    def move_to_marketplace(self):
        self._move_to_kebab()
        self._click(self.MARKETPLACE)
        self._reset_cursor()

    def _reset_cursor(self):
        self.actions.pause(1).move_by_offset(-10, -10).perform()

    def _move_to_kebab(self):
        self.actions.pause(1).move_to_element(self._find_element(self.KEBAB)).perform()

    def _move_to_dropdown(self):
        self.actions.pause(3).click(self._find_element(self.USER_INFO)).perform()
