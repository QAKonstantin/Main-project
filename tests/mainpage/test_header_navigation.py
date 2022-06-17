from pages.api.api_auth import Auth
from pages.elements.header import Header
from pages.base_locators import Locators


def test_navigation_header_by_bo(driver):
    Auth(driver).get_auth_bo_cookie()
    BO = Header(driver)
    BO.move_to_auctions()
    assert BO.check_text_element(
        Locators.TITLE_TRADE).text == 'Торги — Реализация невостребованного имущества', 'Некорректный переход в Торги'
    BO.move_to_catalog()
    assert BO.check_text_element(Locators.TITLE_CATALOG).text == 'Каталог', 'Некорректный переход в Каталог'
    BO.move_to_orders_by_bo()
    assert BO.check_text_element(Locators.TITLE_ORDER).text == 'Заказы', 'Некорректный переход в Заказы'
    BO.move_to_contracts()
    assert BO.check_text_element(Locators.TITLE_TRADE).text == 'Договоры', 'Некорректный переход на страницу в Договоры'
    BO.move_to_contragents()
    assert BO.check_text_element(
        Locators.TITLE_CONTRAGENT).text == 'Контрагенты', 'Некорректный переход на страницу Контрагенты'
    BO.move_to_users()
    assert BO.check_text_element(
        Locators.TITLE_USER).text == 'Пользователи', 'Некорректный переход на страницу Пользователи'


def test_navigation_header_by_user(driver):
    Auth(driver).get_auth_user_cookie()
    user = Header(driver)
    user.move_to_auctions()
    assert user.check_text_element(
        Locators.TITLE_TRADE).text == 'Торги — Реализация невостребованного имущества', 'Некорректный переход в Торги'
    user.move_to_help()
    assert user.check_text_element(Locators.TITLE_HELP).text == 'Помощь', 'Некорректный переход на страницу Помощь'
    user.move_to_orders_by_user()
    assert user.check_text_element(Locators.TITLE_ORDER).text == 'Мои заказы', 'Некорректный переход в Мои заказы'
