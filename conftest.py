import pytest
import os
import logging
import datetime
from pathlib import Path
from selenium.webdriver.chrome.webdriver import WebDriver
from browser import Browser

browser_obj: WebDriver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Check browser")
    parser.addoption("--bversion", action="store", default="101.0", help="Version browser")
    parser.addoption("--kk_url", action="store", default="https://id-preprod.etpgpb.ru", help="Keycloak url")
    parser.addoption("--url", action="store", default="https://reserve-preprod.isource.ru/", help="Start with url")
    parser.addoption("--executor", action="store", default="192.168.0.100", help="Local executor")  # 192.168.0.100
    parser.addoption("--drivers", action="store", default=os.path.expanduser("C:/driver"), help="Path to driver")
    parser.addoption("--headless", action="store_true", default=False, help="Headless mode")
    parser.addoption("--remote", action="store_true", default=False, help="Remote mode")
    parser.addoption("--log_level", action="store", default="INFO", help="Set log level")


@pytest.fixture
def driver(request):
    global browser_obj

    if not browser_obj:
        browser_obj = Browser(request)
        browser_obj = browser_obj.get_driver()
        setup_logger()

    browser_obj.switch_to.window(browser_obj.window_handles[0])
    current_window_handle = browser_obj.current_window_handle
    for handle in browser_obj.window_handles:
        if handle != current_window_handle:
            browser_obj.switch_to.window(handle)
            browser_obj.close()
    browser_obj.switch_to.window(current_window_handle)

    request.addfinalizer(close_driver)
    return browser_obj


def setup_logger():
    setup_logger = logging.getLogger('driver')
    setup_logger.addHandler(
        logging.FileHandler(f"{Path(__file__).resolve().parent}/tests/logs/{browser_obj.test_name}.log", mode='w'))
    setup_logger.setLevel(level=browser_obj.log_level.upper())
    setup_logger.info(
        "===> Test {} started at {}".format(browser_obj.test_name,
                                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    setup_logger.info("Browser:{}".format(browser_obj.browser))
    setup_logger.removeHandler(setup_logger.handlers[0])


def close_driver():
    global browser_obj
    if browser_obj is not None:
        with open(f"{Path(__file__).resolve().parent}/allure-results/environment.properties", 'w') as f:
            f.write(f'Browser={browser_obj.browser}\n')
            f.write(f'Executor={browser_obj.executor}')
        teardown_logger = logging.getLogger('fin')
        teardown_logger.addHandler(
            logging.FileHandler(f"{Path(__file__).resolve().parent}/tests/logs/{browser_obj.test_name}.log"))
        teardown_logger.info(
            "===> Test {} finished at {}".format(browser_obj.test_name,
                                                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        teardown_logger.removeHandler(teardown_logger.handlers[0])
        browser_obj.delete_all_cookies()
        browser_obj.quit()
        browser_obj = None
