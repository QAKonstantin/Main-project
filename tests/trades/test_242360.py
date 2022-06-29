import allure
import pytest
from pages.api.api_auth import Auth
from pages.trades import Trades
from pages.auction_card import Auction
from pages.elements.header import Header


@pytest.mark.regress
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("Ролевая модель")
@allure.suite("Покупатель аккредитованный")
@allure.sub_suite("Товары с уценкой")
@allure.description_html(
    """<a href="http://testrail.etpgpb.local/index.php?/cases/view/242360" target="_blank">Testrail C242360</a>"""
)
@allure.title("Избранное")
def test_favorites(driver):
    Auth(driver).get_auth_user_cookie()
    Header(driver).move_to_auctions()
    user = Trades(driver)
    user.set_favorites()
    user.move_to_auction_card(1)
    Auction(driver).set_favorites_from_card()
    user.setter_favorites_filter()
    assert user.check_elements(user.ACTIVE_FAVORITE) == 2, "Процедуры не были добавлены в Избранное"
    user.unset_favorites()
    user.setter_favorites_filter()
    assert user.check_elements(user.ACTIVE_FAVORITE) == 0, "Процедуры не были удалены из Избранного"
