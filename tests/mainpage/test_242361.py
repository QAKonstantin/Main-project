import allure
import pytest
from pages.api.api_auth import Auth
from pages.elements.alerts import Alerts
from pages.elements.header import Header


@pytest.mark.regress
@allure.severity(allure.severity_level.NORMAL)
@allure.parent_suite("Ролевая модель")
@allure.suite("Покупатель аккредитованный")
@allure.sub_suite("Товары с уценкой")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/242361" target="_blank">Testrail C242361</a>"""
)
@allure.title("Управление подписками")
def test_subscription_management(driver):
    Auth(driver).get_auth_user_cookie()
    Header(driver).open_subscription_management()
    user = Alerts(driver)
    user.cancel_all_categories()
    user.choose_all_categories()
    user.confirm_alert()
    Header(driver).open_subscription_management()
    assert user.check_checkboxes(Alerts.CHECKBOX)[0] == user.check_elements(Alerts.CHECKBOX), \
        "Категории подписки должны сохраняться после подтверждения изменений"
    user.cancel_all_categories()
    user.cancel_alert()
    Header(driver).open_subscription_management()
    assert user.check_checkboxes(Alerts.CHECKBOX)[0] == user.check_elements(Alerts.CHECKBOX), \
        "Категории подписки не должны сохраняться после отмены изменений"
    user.unset_checkbox(2)
    user.confirm_alert()
    Header(driver).open_subscription_management()
    assert user.check_checkboxes(Alerts.CHECKBOX)[1] == 1, \
        "1 категория должна быть неактивна"
    user.cancel_all_categories()
    user.confirm_alert()
    Header(driver).open_subscription_management()
    assert user.check_checkboxes(Alerts.CHECKBOX)[1] == user.check_elements(Alerts.CHECKBOX), \
        "Категории подписки должны сохраняться после подтверждения изменений"
