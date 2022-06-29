from selenium.webdriver.common.by import By
from pages.accreditation.locators.accreditation_base import Accreditation_set


class Accreditation_ip(Accreditation_set):
    OGRN = (By.CSS_SELECTOR, "input[formcontrolname='ogrn']")
    # Ввод данных контрагента
    LOCALITY = (By.CSS_SELECTOR, "input[formcontrolname='locality']")
    LAST_NAME = (By.CSS_SELECTOR, "input[formcontrolname='last_name']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[formcontrolname='first_name']")
    PATRONYMIC = (By.CSS_SELECTOR, "input[formcontrolname='patronymic']")

    # 3 шаг
    PERSONAL_DATA_DOC = (By.XPATH, "//a[contains(text(), ' Согласие на обработку персональных данных ')]")
    CHAIN_OWNERSHIP_DOC = (By.XPATH, "//a[contains(text(), ' Сведения о цепочке собственников ')]")
