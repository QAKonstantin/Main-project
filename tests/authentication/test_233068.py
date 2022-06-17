import allure
import pytest
from pages.main_page import MainPage
from pages.keycloak import Keycloak
from pages.elements.alerts import Alerts
from pages.elements.header import Header


@pytest.mark.regress
@pytest.mark.auth
@allure.parent_suite("Авторизация и Регистрация. Личный кабинет")
@allure.suite("Регистрация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/233068" target="_blank">Testrail C233068</a>"""
)
@allure.title("Прохождение регистрации")
def test_registration(driver):
    MainPage(driver).move_to_keycloak()
    user = Keycloak(driver)
    user.move_to_registration()
    user.input_register_form()
    user.submit_register()
    assert user.check_element(user.MAIL_NOTIFICATION_PAGE)
    assert user.check_element(user.MAIL_NOTIFICATION_ALERT)
    user.email_confirmation()
    Alerts(driver).close_alert()
    assert user.check_element(Header(driver).USER_INFO)
    assert user.check_text_element(MainPage(driver).USER_ROLE).text == 'Покупатель'
