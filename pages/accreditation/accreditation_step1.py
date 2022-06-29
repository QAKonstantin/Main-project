import allure
from selenium.common.exceptions import NoSuchElementException
from pages.accreditation.accreditation_page import Accreditation
from selenium.webdriver.support.ui import Select


class Accreditation_step1(Accreditation):

    @allure.step("Выбрать тип контрагента {type}")
    def choose_type_of_contragent(self, type: str):
        try:
            Select(self._find_element(Accreditation.CONTRAGENT_TYPE)).select_by_value(type)
        except NoSuchElementException:
            self.allure_attach()
            raise AssertionError(f"Отсутствует тип контрагента {type}")

    @allure.step("Заполнение данных на 1 шаге аккредитации для ЮЛ")
    def preinput_accreditation_form_ul(self):
        self._input_text(Accreditation.INN, f"{self.random_with_N_digits(10)}")
        self._input_text(Accreditation.KPP, f"{self.random_with_N_digits(10)}")
        self._click(Accreditation.CONTINUE)

    @allure.step("Заполнение данных на 1 шаге аккредитации для ФЛ")
    def preinput_accreditation_form_fiz(self):
        self._click(Accreditation.CONTINUE)

    @allure.step("Заполнение данных на 1 шаге аккредитации для ИП")
    def preinput_accreditation_form_ip(self):
        self._input_text(Accreditation.INN, f"{self.random_with_N_digits(12)}")
        self._input_text(Accreditation.OGRN, f"{self.random_with_N_digits(15)}")
        self._click(Accreditation.CONTINUE)
