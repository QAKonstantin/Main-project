from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators(BasePage):
    NOTIFY_TITLE = (By.CSS_SELECTOR, ".notify-list-title")
    TITLE_TRADE = (By.CSS_SELECTOR, ".auction-title-text")
    TITLE_CATALOG = (By.CSS_SELECTOR, ".catalog__title")
    TITLE_ORDER = (By.CSS_SELECTOR, ".orders .header")
    TITLE_CONTRAGENT = (By.CSS_SELECTOR, ".contragent-list-title-text")
    TITLE_USER = (By.CSS_SELECTOR, ".content .title")
    TITLE_HELP = (By.CSS_SELECTOR, ".content .top-slider-item__title")
    DISPLAY_TABLE_SHORT = (By.XPATH, "//span[contains(text(), ' Таблица кратко ')]")
    DISPLAY_TABLE_DETAILED = (By.XPATH, "//span[contains(text(), ' Таблица подробно ')]")
    CONTINUE = (By.XPATH, "//span[text()=' Продолжить ']")
    NOTIFY_CLEAR_CLOSE = (By.XPATH, "//span[text()='Закрыть и очистить']")
