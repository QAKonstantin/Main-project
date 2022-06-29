import allure
import pytest

from pages.elements.footer import Footer


@pytest.mark.regress
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка наличия всех файлов и ссылок на главной странице")
def test_navigation_footer_by_guest(driver):
    guest = Footer(driver)
    guest.move_to_footer()
    guest.check_footer_urls()
