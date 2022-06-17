import os
import allure
import pytest
from pages.accreditation.accreditation_step1 import Accreditation_step1
from pages.accreditation.accreditation_step2 import Accreditation_step2
from pages.accreditation.accreditation_step3 import Accreditation_step3
from pages.elements.header import Header
from pages.keycloak import Keycloak
from pages.main_page import MainPage
from pages.elements.notifications import Notifications
from pages.trades import Trades


@pytest.mark.accreditation
@pytest.mark.regress
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("Регрессионная модель")
@allure.suite("Аккредитация")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/271455" target="_blank">Testrail C271455</a>"""
)
@allure.title("Аккредитация ФЛ")
def test_accreditation_fiz_by_user(driver):
    MainPage(driver).move_to_keycloak()
    Keycloak(driver).registration()
    Header(driver).move_to_auctions()
    user = Trades(driver)
    user.change_table_display_to_detailed()
    user.get_accreditation()
    with allure.step("1 шаг аккредитации"):
        Accreditation_step1(driver).choose_type_of_contragent("FIZ")
        Accreditation_step1(driver).preinput_accreditation_form_fiz()
    with allure.step("2 шаг аккредитации"):
        Accreditation_step2(driver).input_accreditation_form_fiz()
    with allure.step("3 шаг аккредитации"):
        Accreditation_step3(driver).agree_with_rules()
        Accreditation_step3(driver).upload_document_accreditation()
    assert Notifications(driver).check_notification("Файл(ы) успешно загружен(ы)"), \
        "Файл не загружен"
    Notifications(driver).clear_and_close_notification()
    Accreditation_step3(driver).check_url(Accreditation_step3.WORK_RULES, os.getenv("WORK_RULES"))


@pytest.mark.accreditation
@pytest.mark.regress
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("Регрессионная модель")
@allure.suite("Аккредитация")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/271451" target="_blank">Testrail C271451</a>"""
)
@allure.title("Аккредитация ЮЛ")
def test_accreditation_ul_by_user(driver):
    MainPage(driver).move_to_keycloak()
    Keycloak(driver).registration()
    Header(driver).move_to_auctions()
    user = Trades(driver)
    user.change_table_display_to_detailed()
    user.get_accreditation()
    with allure.step("1 шаг аккредитации"):
        Accreditation_step1(driver).choose_type_of_contragent("UR")
        Accreditation_step1(driver).preinput_accreditation_form_ul()
    with allure.step("2 шаг аккредитации"):
        Accreditation_step2(driver).input_accreditation_form_ul()
    with allure.step("3 шаг аккредитации"):
        Accreditation_step3(driver).agree_with_rules()
        Accreditation_step3(driver).upload_document_accreditation()
    assert Notifications(driver).check_notification("Файл(ы) успешно загружен(ы)"), \
        "Файл не загружен"
    Notifications(driver).clear_and_close_notification()
    Accreditation_step3(driver).check_url(Accreditation_step3.WORK_RULES, os.getenv("WORK_RULES"))
    Accreditation_step3(driver).send_application()


@pytest.mark.accreditation
@pytest.mark.regress
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("Регрессионная модель")
@allure.suite("Аккредитация")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/271446" target="_blank">Testrail C271446</a>"""
)
@allure.title("Аккредитация ИП")
def test_accreditation_ip_by_user(driver):
    MainPage(driver).move_to_keycloak()
    Keycloak(driver).registration()
    Header(driver).move_to_auctions()
    user = Trades(driver)
    user.change_table_display_to_detailed()
    user.get_accreditation()
    with allure.step("1 шаг аккредитации"):
        Accreditation_step1(driver).choose_type_of_contragent("IP")
        Accreditation_step1(driver).preinput_accreditation_form_ip()
    with allure.step("2 шаг аккредитации"):
        Accreditation_step2(driver).input_accreditation_form_ip()
    with allure.step("3 шаг аккредитации"):
        Accreditation_step3(driver).agree_with_rules()
        Accreditation_step3(driver).upload_document_accreditation()
    assert Notifications(driver).check_notification("Файл(ы) успешно загружен(ы)"), \
        "Файл не загружен"
    Notifications(driver).clear_and_close_notification()
    Accreditation_step3(driver).check_url(Accreditation_step3.WORK_RULES, os.getenv("WORK_RULES"))
