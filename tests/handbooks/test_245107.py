import allure
import os
import pytest
from pages.main_page import MainPage
from pages.handbooks_page import Warehouse
from pages.elements.notifications import Notifications
from pages.elements.header import Header


@pytest.mark.regress
@pytest.mark.warehouse
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("Справочники")
@allure.suite("Справочник складов")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/245107" target="_blank">Testrail C245107</a>"""
)
@allure.title("Создание склада с незаполненным кодом")
def test_wh_filled_code(driver):
    BO = MainPage(driver)
    BO.login_with(os.getenv("admin_email1"), os.getenv("admin_password"))
    assert BO.check_element(Header(driver).USER_INFO), "Пользователь не авторизован"
    BO.move_to_handbooks()
    BO = Warehouse(driver)
    BO.move_to_warehouse()
    BO.add_to_warehouse()
    BO.input_wh_form()
    assert Notifications(driver).check_notification("Запись склада успешно создана"), \
        "Склад не создан"
