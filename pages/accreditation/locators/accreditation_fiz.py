from selenium.webdriver.common.by import By
from pages.accreditation.locators.accreditation_ip import Accreditation_ip


class Accreditation_fiz(Accreditation_ip):
    # Ввод данных контрагента
    PASSPORT_SERIAL = (By.CSS_SELECTOR, "input[formcontrolname='passport_serial']")
    PASSPORT_ISSUE_BY = (By.CSS_SELECTOR, "input[formcontrolname='passport_issue_by']")
    PASSPORT_ISSUE_DATE = (By.CSS_SELECTOR, "input[placeholder='Дата выдачи паспорта']")
