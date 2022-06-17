import allure
import os
import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.elements.alerts import Alerts
from selenium.webdriver.common.keys import Keys
from faker import Faker


class Keycloak(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#password-confirm")
    SUBMIT = (By.CSS_SELECTOR, "#kc-form-buttons")
    REGISTRATION = (By.CSS_SELECTOR, "a[onclick='clickYaRegisterLink();']")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PHONE = (By.CSS_SELECTOR, "[name='user.attributes.mobile']")
    LASTNAME = (By.CSS_SELECTOR, "#lastName")
    FIRSTNAME = (By.CSS_SELECTOR, "#firstName")
    PATRONYMIC = (By.CSS_SELECTOR, "[name='user.attributes.patronymic']")
    GENERAL_AGREEMENT = (By.CSS_SELECTOR, "[name='user.attributes.generalAgreement']")
    REGISTER = (By.CSS_SELECTOR, "#submit_register")
    MAIL_NOTIFICATION_ALERT = (By.CSS_SELECTOR, ".card-pf")
    MAIL_NOTIFICATION_PAGE = (By.CSS_SELECTOR, ".login-pf-page")
    CHECK_MAIL = (By.CSS_SELECTOR, "#button")
    MAIL_MESSAGE_BODY = (By.CSS_SELECTOR, "#messagebody")

    @allure.step("Перейти на страницу регистрации")
    def move_to_registration(self):
        self._click(self.REGISTRATION)

    @allure.step("Ввести данные на форме регистрации")
    def input_register_form(self):
        self.faker_ru = Faker('ru_RU')
        self.faker_eng = Faker()
        self.full_name = self.faker_eng.name().split()
        self.email = f"{self.full_name[1]}{self.faker_eng.random_int(1920, 2004)}"
        self._input_text(self.EMAIL, f"{self.email}@mailforspam.com")
        self._input_text(self.PHONE, self.faker_ru.phone_number())
        self._input_text(self.LASTNAME, self.full_name[0])
        self._input_text(self.FIRSTNAME, self.full_name[1])
        self._input_text(self.PATRONYMIC, self.full_name[0])
        self._input_text(self.PASSWORD, os.getenv("user_password"))
        self._find_element(self.PASSWORD).send_keys(Keys.TAB)
        self._input_text(self.PASSWORD_CONFIRM, os.getenv("user_password"))
        self._click(self.GENERAL_AGREEMENT)

    @allure.step("Подтверждение email")
    def email_confirmation(self):
        self.browser.get(f"http://mailforspam.com/mail/{self.email}")
        self._click(self.CHECK_MAIL)
        self.waiting(self._search_link_text(
            "Подтверждение регистрации на платформе Isource")).click()
        self.url = re.search(r'http(.+?)mail', self._find_element(self.MAIL_MESSAGE_BODY).text)
        self.browser.get(self.url.group(0))

    @allure.step("Согласие на подтверждение почты")
    def submit_register(self):
        self.submit(self.REGISTER)

    @allure.step("Регистрация пользователя")
    def registration(self):
        self.move_to_registration()
        self.input_register_form()
        self.submit_register()
        self.email_confirmation()
        Alerts(self.browser).close_alert()
