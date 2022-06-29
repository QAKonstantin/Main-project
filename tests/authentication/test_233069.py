import allure
import os
import pytest
from pages.main_page import MainPage
from pages.elements.header import Header
from pages.api.api_auth import Auth


@pytest.mark.regress
@pytest.mark.auth
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("Авторизация и Регистрация. Личный кабинет")
@allure.suite("Авторизация")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/233069" target="_blank">Testrail C233069</a>"""
)
@allure.title("Прохождение авторизации")
def test_authorization(driver):
    user = MainPage(driver)
    user.login_with(os.getenv("user_email1"), os.getenv("user_password"))
    assert user.check_element(Header(driver).USER_INFO), "Пользователь не авторизован"


@allure.title("Авторизация через cookie")
def test_auth_with_cookie(driver):
    user = Auth(driver)
    user.get_auth_user_cookie()
    assert MainPage(driver).check_element(Header(driver).USER_INFO), "Пользователь не авторизован"
