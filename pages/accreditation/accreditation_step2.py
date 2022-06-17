import allure
from pages.accreditation.accreditation_page import Accreditation


class Accreditation_step2(Accreditation):
    @allure.step("Заполнение данных на 2 шаге аккредитации для ЮЛ")
    def input_accreditation_form_ul(self):
        # Ввод данных контрагента
        self._input_text(Accreditation.SHORT_NAME_COMPANY, "Краткое наименование организации")
        self._input_text(Accreditation.FULL_NAME_COMPANY, "Полное наименование организации")
        self._input_text(Accreditation.COMPANY_LIDER, "ФИО руководителя организации")
        self._input_text(Accreditation.POSITION, "Ваша должность в организации")
        self._input_text(Accreditation.POSITION_GENITIVE, "Должность руководителя в родительном падеже")
        self.input_bank_details(1)
        self.input_all_addresses(1)
        self._click(Accreditation.CONTINUE)

    @allure.step("Заполнение данных на 2 шаге аккредитации для ФЛ")
    def input_accreditation_form_fiz(self):
        # Ввод данных контрагента
        self._input_text(Accreditation.PASSPORT_SERIAL, "12 34 567890")
        self._input_text(Accreditation.PASSPORT_ISSUE_BY, "УФМС России")
        self._input_text(Accreditation.PASSPORT_ISSUE_DATE, "19.06.2015")
        self.input_bank_details(0)
        self.input_legal_address(0)
        self._click(Accreditation.CONTINUE)

    @allure.step("Заполнение данных на 2 шаге аккредитации для ИП")
    def input_accreditation_form_ip(self):
        # Ввод данных контрагента
        self._input_text(Accreditation.LOCALITY, "Москва")
        self.temporary_input_text(Accreditation.PASSPORT_SERIAL, "12 34 567890", 1)
        self.temporary_input_text(Accreditation.PASSPORT_ISSUE_BY, "УФМС России", 1)
        self.temporary_input_text(Accreditation.PASSPORT_ISSUE_DATE, "19.06.2015", 1)
        self.temporary_input_text(Accreditation.POSITION, "Ваша должность в организации", 1)
        self.temporary_input_text(Accreditation.POSITION_GENITIVE, "Должность руководителя в родительном падеже", 1)
        self.input_bank_details(2)
        self.input_legal_address(2)
        self._click(Accreditation.CONTINUE)

    @allure.step("Заполнить банковские реквизиты")
    def input_bank_details(self, type):
        # Банковские реквизиты
        self.temporary_input_text(Accreditation.BIK, "044030814", type)
        self.temporary_input_text(Accreditation.CHECKING_ACCOUNT, "36857546253315521512", type)
        self.temporary_input_text(Accreditation.COR_ACCOUNT, "30101810200000000814", type)
        self.temporary_input_text(Accreditation.BANK_NAME, "АО «ГОРБАНК»", type)
        self.temporary_input_text(Accreditation.BANK_ADDRESS,
                                  "191186, г Санкт-Петербург, Центральный р-н, ул Итальянская, д 15 литера а", type)

    @allure.step("Заполнить юридический адрес")
    def input_legal_address(self, type):
        # Юридический адрес
        self.temporary_input_text(Accreditation.UR_INDEX, "111111", type)
        self.temporary_input_text(Accreditation.UR_COUNTRY, "Россия_Юр_адрес", type)
        self.temporary_input_text(Accreditation.UR_REGION, "Московский_Юр_адрес", type)
        self.temporary_input_text(Accreditation.UR_CITY, "Москва_Юр_адрес", type)
        self.temporary_input_text(Accreditation.UR_STREET, "Московская_Юр_адрес", type)
        self.temporary_input_text(Accreditation.UR_HOUSE, "1_Юр_адрес", type)
        self.temporary_input_text(Accreditation.UR_APARTMENT, "2_Юр_адрес", type)

    @allure.step("Заполнить фактический адрес")
    def input_actual_address(self):
        # Фактический адрес
        self._input_text(Accreditation.ACTUAL_INDEX, "222222")
        self._input_text(Accreditation.ACTUAL_COUNTRY, "Россия_факт_адрес")
        self._input_text(Accreditation.ACTUAL_REGION, "Московский_факт_адрес")
        self._input_text(Accreditation.ACTUAL_CITY, "Москва_факт_адрес")
        self._input_text(Accreditation.ACTUAL_STREET, "Московская_факт_адрес")
        self._input_text(Accreditation.ACTUAL_HOUSE, "1_факт_адрес")
        self._input_text(Accreditation.ACTUAL_APARTMENT, "2_факт_адрес")

    @allure.step("Заполнить почтовый адрес")
    def input_post_address(self):
        # Почтовый адрес
        self._input_text(Accreditation.POST_INDEX, "333333")
        self._input_text(Accreditation.POST_COUNTRY, "Россия_почт_адрес")
        self._input_text(Accreditation.POST_REGION, "Московский_почт_адрес")
        self._input_text(Accreditation.POST_CITY, "Москва_почт_адрес")
        self._input_text(Accreditation.POST_STREET, "Московская_почт_адрес")
        self._input_text(Accreditation.POST_HOUSE, "1_почт_адрес")
        self._input_text(Accreditation.POST_APARTMENT, "2_почт_адрес")

    def input_all_addresses(self, type):
        self.input_legal_address(type)
        self.input_actual_address()
        self.input_post_address()
