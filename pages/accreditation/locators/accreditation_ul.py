from selenium.webdriver.common.by import By
from pages.accreditation.locators.accreditation_base import Accreditation_set


class Accreditation_ul(Accreditation_set):
    KPP = (By.CSS_SELECTOR, "input[formcontrolname='kpp']")
    # Ввод данных контрагента
    SHORT_NAME_COMPANY = (By.CSS_SELECTOR, "input[formcontrolname='short_company_name']")
    FULL_NAME_COMPANY = (By.CSS_SELECTOR, "input[formcontrolname='full_company_name']")
    COMPANY_LIDER = (By.CSS_SELECTOR, "input[formcontrolname='company_lider']")

    # Фактический адрес
    ACTUAL_ADDRESS_FILLER = (By.CSS_SELECTOR, "label[formcontrolname='actual_address_filler'] input")
    ACTUAL_INDEX = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_index']")
    ACTUAL_COUNTRY = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_country']")
    ACTUAL_REGION = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_region']")
    ACTUAL_CITY = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_city']")
    ACTUAL_STREET = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_street']")
    ACTUAL_HOUSE = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_house']")
    ACTUAL_APARTMENT = (By.CSS_SELECTOR, "input[formcontrolname='actual_address_apartment']")

    # Почтовый адрес
    POST_ADDRESS_ACTUAL_FILLER = (
        By.CSS_SELECTOR, "label[formcontrolname='post_address_actual_filler'] input")
    POST_ADDRESS_FILLER = (By.CSS_SELECTOR, "label[formcontrolname='post_address_filler'] input")
    POST_INDEX = (By.CSS_SELECTOR, "input[formcontrolname='post_address_index']")
    POST_COUNTRY = (By.CSS_SELECTOR, "input[formcontrolname='post_address_country']")
    POST_REGION = (By.CSS_SELECTOR, "input[formcontrolname='post_address_region']")
    POST_CITY = (By.CSS_SELECTOR, "input[formcontrolname='post_address_city']")
    POST_STREET = (By.CSS_SELECTOR, "input[formcontrolname='post_address_street']")
    POST_HOUSE = (By.CSS_SELECTOR, "input[formcontrolname='post_address_house']")
    POST_APARTMENT = (By.CSS_SELECTOR, "input[formcontrolname='post_address_apartment']")
