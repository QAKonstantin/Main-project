import time

import allure
from pages.accreditation.accreditation_page import Accreditation
from pages.elements.alerts import Alerts


class Accreditation_step3(Accreditation):

    @allure.step("Согласиться с правилами работы")
    def agree_with_rules(self):
        time.sleep(2)
        Alerts(self.browser).set_checkbox(0)

    @allure.step("Открыть шаблоны документов")
    def open_documents_template(self, type):
        if type.lower() == 'ip':
            self._click(Accreditation.CHAIN_OWNERSHIP_DOC)
            self._click(Accreditation.PERSONAL_DATA_DOC)
        elif type.lower() == 'fiz':
            self._click(Accreditation.PERSONAL_DATA_DOC)

    def upload_document_accreditation(self):
        self.upload_document("C:/Development/reserve/files/oferta.pdf", "oferta.pdf")

    @allure.step("Отправить заявку на аккредитацию")
    def send_application(self):
        self._click(self.SEND_APPLICATION)
