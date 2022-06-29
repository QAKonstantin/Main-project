import allure
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Footer(BasePage):
    FOOTER = (By.CSS_SELECTOR, ".footer")
    PROCESSOR = (By.XPATH, "//a[text()='Processor']")
    RESERVE = (By.XPATH, "//span[text()='Reserve']")
    INSPECTOR = (By.XPATH, "//a[text()='Inspector']")
    RADAR = (By.XPATH, "//a[text()='Radar']")
    ELEMENT = (By.XPATH, "//a[text()='Element']")
    ISOURCE = (By.XPATH, "//a[text()='Isource']")
    TASKS_ISOURCE = (By.XPATH, "//a[text()='Основные задачи Isource']")
    PRODUCTS = (By.XPATH, "//a[text()='Продукты']")
    BANK_GUARANTEES = (By.XPATH, "//a[text()='Банковские гарантии']")
    DYNAMIC_DISCOUNT = (By.XPATH, "//a[text()='Динамическое дисконтирование']")
    USER_MANUAL = (By.XPATH, "//a[text()='Руководство пользователя']")
    MARKING_NOTE = (By.XPATH, "//a[text()='Памятка по маркировке']")
    FOOTER_EXPAND = (By.CSS_SELECTOR, ".footer-downloads__expand")
    RESERVE_INSTRUCTION = (By.XPATH, "//a[text()='Инструкция Резерва']")
    RESERVE_RULES = (By.XPATH, "//a[text()='Правила Резерва']")
    PROCESSING_POLICY = (By.XPATH, "//a[text()='Политика обработки персональных данных АО ЦЗС']")
    LOGO_ISOURCE = (By.CSS_SELECTOR, ".footer-desing .icon")

    def check_footer_urls(self):
        self.check_url(self.PROCESSOR, "https://passport.isource.ru/")
        self.check_url(self.INSPECTOR, "https://inspector.isource.ru/")
        self.check_url(self.RADAR, "https://radar.isource.ru/")
        self.check_url(self.ELEMENT, "https://passport.isource.ru/")
        self.check_url(self.ISOURCE, "https://www.isource.ru/about/")
        self.check_url(self.TASKS_ISOURCE, "https://www.isource.ru/about/#main-tasks")
        self.check_url(self.PRODUCTS, "https://www.isource.ru/#products")
        self.check_url(self.BANK_GUARANTEES, "https://www.isource.ru/bank-products/bank-guarantees.php")
        self.check_url(self.DYNAMIC_DISCOUNT, "https://www.isource.ru/bank-products/dynamic-discounting.php")
        self.check_url(self.USER_MANUAL, os.getenv("USER_MANUAL"))
        self.check_url(self.MARKING_NOTE, os.getenv("MARKING_NOTE"))
        self.footer_expand()
        self.check_url(self.RESERVE_INSTRUCTION, os.getenv("RESERVE_INSTRUCTION"))
        self.check_url(self.RESERVE_RULES, os.getenv("RESERVE_RULES"))
        self.check_url(self.PROCESSING_POLICY, os.getenv("PROCESSING_POLICY"))
        self.check_url(self.LOGO_ISOURCE, "https://www.isource.ru/")
        self.open_reserve()

    @allure.step("Открыть url Резерва")
    def open_reserve(self):
        self._click(self.RESERVE)
        self.check_current_url(self.browser.url)
        self.check_scrolling()

    @allure.step("Проскроллить до футера")
    def move_to_footer(self):
        return self.browser.execute_script('arguments[0].scrollIntoView(true);', self._find_element(self.FOOTER))

    @allure.step("Развернуть документы в футере")
    def footer_expand(self):
        self._click(self.FOOTER_EXPAND)
