import logging
import time
from contextlib import contextmanager
from random import randint

import allure
from dotenv import load_dotenv
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, JavascriptException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=30):
        self.browser = driver
        self.__config_logger()
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)
        self.count = 0
        load_dotenv()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.fh = logging.FileHandler(
            f"{Path(__file__).resolve().parent.parent}/tests/logs/{self.browser.test_name}.log")
        self.fh.setFormatter(
            logging.Formatter(fmt='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S'))
        self.logger.addHandler(self.fh)
        self.logger.setLevel(level=self.browser.log_level)
        if len(self.logger.handlers) != 1:
            self.logger.removeHandler(self.logger.handlers[0])

    def remove_logger(self):
        self.logger.removeHandler(self.logger.handlers[0])

    def waiting(self, element, timeout=5):
        if (element):
            return element
        elif self.count <= timeout:
            time.sleep(timeout)
            self.count += 1
            self.waiting()
        else:
            self.logger.warning("Элемент не найден: {}".format(element))
            raise AssertionError("Элемент не найден: {}".format(element))

    @allure.step("Открыть ссылку {path}")
    def open(self, path):
        self.logger.info("Открыть url: {}".format(self.browser.url + path))
        self.browser.get(self.browser.current_url + path)
        return self

    @allure.step("Нажать на элемент '{locator}'")
    def _click(self, locator: tuple, timeout=10):
        try:
            self.wait_ajax()
            self.logger.info(f"Нажать на элемент: {locator}")
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)).click()
        except (StaleElementReferenceException, TimeoutException):
            self.logger.warning(f"Невозможно нажать на элемент {locator}")
            self.allure_attach()
            raise AssertionError((f"Невозможно нажать на элемент '{locator}'"))

    @allure.step("Двойное нажатие на элемент '{locator}'")
    def _dclick(self, locator: tuple):
        self.element = self._find_element(locator)
        self.logger.info(f"Двойное нажатие на элемент: {locator}")
        self.actions.double_click(self.element).perform()

    # @contextmanager
    # def wait_for_page_load(self, timeout=10):
    #     self.logger.debug(f"Waiting for page to load at {self.browser.current_url}")
    #     old_page = self.browser.find_element_by_tag_name('html')
    #     yield
    #     WebDriverWait(self.browser, timeout).until(EC.staleness_of(old_page))

    # def wait_for_page_load2(self):
    #     self.logger.debug(f"Waiting for page to load at {self.browser.current_url}")
    #     page_state = self.browser.execute_script('return document.readyState;')
    #     return page_state == 'complete'

    def wait_ajax(self):
        try:
            ajax_status = self.wait.until(lambda browser: self.browser.execute_script(
                'return !Ext.Ajax.isLoading() && Ext.query(".x-mask-loading").length==0;'))
            return ajax_status
        except JavascriptException:
            """Message: javascript error: Ext os not defined"""
            pass

    @allure.step("Загрузить документ '{fileName}'")
    def upload_document(self, filePath, fileName):
        self.browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(filePath)

    @allure.step("Открыть url '{url}'")
    def check_url(self, locator, url):
        self._click(locator)
        self.check_number_handles()
        self.check_current_url(url)
        self.close_current_handle()

    @allure.step("Поиск элемента: '{locator}'")
    def _find_element(self, locator: tuple, timeout=10):
        try:
            self.logger.info("Проверить наличие элемента {}".format(locator))
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.warning("Не найден элемент по локатору: {}".format(locator))
            self.allure_attach()
            raise AssertionError(f"Не найден элемент по локатору: {locator}")

    @allure.step("Поиск элементов: '{locator}'")
    def _find_elements(self, locator: tuple):
        self.browser.implicitly_wait(5)
        self.logger.info("Проверить наличие элементов {}".format(locator))
        return self.browser.find_elements(*locator)

    @allure.step("Search link text: '{link_text}'")
    def _search_link_text(self, link_text, timeout=30):
        try:
            self.logger.info("Проверить на наличие текста '{}'".format(link_text))
            return WebDriverWait(self.browser, timeout) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            self.logger.warning("Невозможно найти элемент по тексту: '{}'".format(link_text))
            self.allure_attach()
            raise AssertionError(f"Невозможно найти элемент по тексту: {link_text}")

    @allure.step("Ожидание элемента с текстом: '{goal}'")
    def _wait_text_element(self, locator: tuple, goal: str, timeout=30):
        self.logger.info(f"Проверка отображения элемента{locator}")
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, goal))
        except TimeoutException:
            self.allure_attach()
            raise AssertionError(f"Невозможно найти элемент по локатору: {locator}")

    def allure_attach(self):
        allure.attach(
            name=self.browser.session_id,
            body=self.browser.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Ввести текст: '{text}'")
    def _input_text(self, locator: tuple, text):
        web_element = self._find_element(locator)
        self.logger.info(f"Ввести '{text}'")
        web_element.click()
        # web_element.clear()
        web_element.send_keys(text)

    # Для заполнения форм аккредитации: 0 - ФЛ, 1 - ЮЛ, 2 - ИП
    @allure.step("Ввод текста: '{text}'")
    def temporary_input_text(self, locator: tuple, text, type):
        web_element = self._find_elements(locator)[type]
        self.logger.info(f"Ввести '{text}'")
        web_element.click()
        web_element.send_keys(text)

    @allure.step("Проверить элемент: '{locator}'")
    def check_element(self, locator: tuple):
        try:
            self._find_element(locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step("Проверить текст элемента: '{locator}'")
    def check_text_element(self, locator: tuple):
        time.sleep(3)
        return self._find_element(locator)

    @allure.step("Проверить элементы: '{locator}'")
    def check_elements(self, locator: tuple):
        return len(self._find_elements(locator))

    @allure.step("Количество активных и неактиных чекбоксов: '{locator}'")
    def check_checkboxes(self, locator: tuple):
        temp = self._find_elements(locator)
        mas = [0, 0]
        for i in range(len(temp)):
            if temp[i].get_attribute("checked") == "true":
                mas[0] += 1
            else:
                mas[1] += 1
        return mas

    @allure.step("Нажать на кнопку: '{locator}'")
    def submit(self, locator: tuple):
        self.element = self._find_element(locator)
        self.logger.info(f"Нажать на кнопку {locator}")
        self.element.click()

    @allure.step("Проверить количество вкладок в браузере")
    def check_number_handles(self):
        if len(self.browser.window_handles) == 2:
            self.browser.switch_to.window(self.browser.window_handles[-1])
            return True
        else:
            raise AssertionError("Некорректное количество вкладок в браузере")

    @allure.step("Закрыть текущую вкладку")
    def close_current_handle(self):
        if len(self.browser.window_handles) > 1:
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
        else:
            raise AssertionError("Невозможно закрыть текущую вкладку")

    @allure.step("Проверить текущую ссылку '{url}'")
    def check_current_url(self, url):
        if url in self.browser.current_url:
            return True
        else:
            raise AssertionError(f"Невозможно проверить текущий url {url}")

    @allure.step("Проверить позицию скроллинга")
    def check_scrolling(self, y=0):
        if self.browser.execute_script("return window.pageYOffset;") == y:
            return True
        else:
            raise AssertionError(f"Некорректная позиция скроллинга, y={y}")

    def random_with_N_digits(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
