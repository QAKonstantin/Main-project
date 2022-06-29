import warnings

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Browser:

    def __init__(self, request):
        self.request = request
        self.browser = self.request.config.getoption("--browser").lower()
        self.url = self.request.config.getoption("--url").lower()
        self.kk_url = self.request.config.getoption("--kk_url").lower()
        self.executor = self.request.config.getoption("--executor").lower()
        self.bversion = self.request.config.getoption("--bversion").lower()

    def get_options(self):
        if self.browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            # chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--auto-open-devtools-for-tabs")
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            if self.request.config.getoption("--headless"):
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--window-size=1920x1080")
        else:
            raise Exception(f"Driver {self.browser} not supported")
        return chrome_options

    def get_driver(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        chrome_options = self.get_options()

        if self.request.config.getoption("--remote"):
            caps = {
                "browserName": self.browser,
                "browserVersion": self.bversion,
                "screenResolution": "1920x1080",
                "name": "AutoTest",
                "selenoid:options": {
                    "sessionTimeout": "10s",
                    "enableVNC": True,
                    "enableVideo": True,
                    "enableLog": True
                }
            }
            _driver = webdriver.Remote(
                command_executor="http://{}:4444/wd/hub".format(self.executor),
                options=chrome_options,
                desired_capabilities=caps)
        else:
            serv = Service(self.request.config.getoption("--drivers").lower() + "/chromedriver")
            _driver = webdriver.Chrome(service=serv, options=chrome_options)
        _driver.browser = self.browser
        _driver.url = self.url
        _driver.kk_url = self.kk_url
        _driver.executor = self.executor
        _driver.test_name = self.request.node.name
        _driver.log_level = self.request.config.getoption("--log_level").upper()
        _driver.maximize_window()
        _driver.get(_driver.url)
        return _driver
