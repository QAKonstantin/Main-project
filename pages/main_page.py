import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.keycloak import Keycloak
from pages.elements.header import Header


class MainPage(BasePage):
    AUTH_BUTTON = (By.CSS_SELECTOR, ".auth-sso .unAuthorized")
    USER_ROLE = (By.XPATH, "//span[text()='Покупатель']")
    HANDBOOKS = (By.XPATH, "//*[contains(text(), ' Справочники ')]")

    @allure.step("Авторизоваться под пользователем {username}")
    def login_with(self, username, password):
        self.move_to_keycloak()
        self._input_text(Keycloak.USERNAME, username)
        self._input_text(Keycloak.PASSWORD, password)
        self._click(Keycloak.SUBMIT)

    @allure.step("Перейти на страницу Авторизации")
    def move_to_keycloak(self):
        self._click(self.AUTH_BUTTON)

    @allure.step("Перейти к справочникам")
    def move_to_handbooks(self):
        Header(self.browser)._move_to_dropdown()
        self.actions.double_click(self._find_element(self.HANDBOOKS)).pause(3).perform()
