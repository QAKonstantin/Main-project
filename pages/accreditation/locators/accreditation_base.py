from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Accreditation_set(BasePage):
    CONTRAGENT_TYPE = (By.CSS_SELECTOR, "select[formcontrolname='type_id']")
    INN = (By.CSS_SELECTOR, "input[formcontrolname='inn']")

    # Ввод данных контрагента
    PHONE = (By.CSS_SELECTOR, "input[formcontrolname='phone']")
    EMAIL = (By.CSS_SELECTOR, "input[formcontrolname='email']")
    POSITION_GENITIVE = (By.CSS_SELECTOR, "input[formcontrolname='position_genitive']")
    POSITION = (By.CSS_SELECTOR, "input[formcontrolname='position']")

    # Банковские реквизиты
    BIK = (By.CSS_SELECTOR, "input[formcontrolname='bik']")
    CHECKING_ACCOUNT = (By.CSS_SELECTOR, "input[formcontrolname='checking_account']")
    COR_ACCOUNT = (By.CSS_SELECTOR, "input[formcontrolname='cor_account']")
    BANK_NAME = (By.CSS_SELECTOR, "input[formcontrolname='bank_name']")
    BANK_ADDRESS = (By.CSS_SELECTOR, "input[formcontrolname='bank_address']")

    # Юридический адрес
    UR_INDEX = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_index']")
    UR_COUNTRY = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_country']")
    UR_REGION = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_region']")
    UR_CITY = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_city']")
    UR_STREET = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_street']")
    UR_HOUSE = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_house']")
    UR_APARTMENT = (By.CSS_SELECTOR, "input[formcontrolname='ur_address_apartment']")

    # 3 шаг
    CHECKBOX_AGREEMENT = (By.CSS_SELECTOR, ".ant-checkbox-inner")
    WORK_RULES = (By.XPATH, "//a[contains(text(), 'правилами работы')]")
    SAVE_AND_COMPLETE_LATER = (By.XPATH, "//span[contains(text(), ' Сохранить и завершить позже ')]")
    SEND_APPLICATION = (By.XPATH, "//span[contains(text(), ' Отправить заявку на аккредитацию ')]")
