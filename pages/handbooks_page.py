import allure
import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Warehouse(BasePage):
    WAREHOUSE = (By.XPATH, "//*[contains(text(), 'Склады')]")
    ADD_WH = (By.CSS_SELECTOR, ".add-button-content")
    WH_ADDRESS = (By.CSS_SELECTOR, "uxg-dropdown-input[formcontrolname='address_dadata']")
    WH_ADDRESS_LIST = (By.CSS_SELECTOR, "div[class='app-dropdown-items-item ng-star-inserted']")
    SUPPLIER_WH = (By.CSS_SELECTOR, "input[formcontrolname='supplier_search']")
    EXTRA_CONDITION = (By.CSS_SELECTOR, "textarea[formcontrolname='extra_conditions']")
    SUPPLIERS_LIST = (By.CSS_SELECTOR, "div[class='ant-select-item-option-content']")
    SUPPLIERS = (By.XPATH, ".cdk-overlay-pane nz-auto-option[role='menuitem']")
    LONGITUDE = (By.NAME, "longitude")
    LATITUDE = (By.NAME, "latitude")
    ICON_TRASH = (By.CSS_SELECTOR, "use[*|href='/assets/images/sprite.svg#trash_alt']")
    CREATE_WH = (By.XPATH, "//*[contains(text(), ' Добавить склад ')]")

    @allure.step("Перейти к справочнику Склады")
    def move_to_warehouse(self):
        self._click(self.WAREHOUSE)

    def add_to_warehouse(self):
        self._click(self.ADD_WH)

    @allure.step("Заполнить форму по складу")
    def input_wh_form(self):
        self.actions.double_click(self._find_element(self.SUPPLIER_WH)).pause(1).perform()
        self.actions.click(self._find_elements(self.SUPPLIERS_LIST)[
                               random.randint(0, len(self._find_elements(self.SUPPLIERS_LIST)) - 1)]).perform()
        self.actions.click(self._find_element(self.WH_ADDRESS)).pause(1).perform()
        self.actions.send_keys_to_element(self._find_element(self.WH_ADDRESS), "12").pause(3).perform()
        self.actions.click(self._find_elements(self.WH_ADDRESS_LIST)[
                               random.randint(0, len(self._find_elements(
                                   self.WH_ADDRESS_LIST)) - 1)]).perform()
        self._input_text(self.LONGITUDE, round(random.uniform(0.001, 180.000), 3))
        self._input_text(self.LATITUDE, round(random.uniform(0.001, 90.000), 3))
        self._input_text(self.EXTRA_CONDITION, 'autotest')
        # self._click(self.ICON_TRASH)
        self._click(self.CREATE_WH)
