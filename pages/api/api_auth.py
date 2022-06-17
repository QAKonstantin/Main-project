import requests
import re
import os
from dotenv import load_dotenv


class Auth:
    def __init__(self, driver):
        self.browser = driver
        load_dotenv()

    def get_token(self):
        data = {"client_id": "NVI-preprod", "grant_type": "password",
                "client_secret": os.getenv("secret_preprod"), "scope": "openid profile email",
                "username": os.getenv("admin_email1"), "password": os.getenv("admin_password")}
        response = requests.post(
            f"{self.browser.kk_url}/auth/realms/master/protocol/openid-connect/token", data)

        return response

    def get_auth_bo_cookie(self):
        session = requests.Session()
        payload = {
            "username": os.getenv("user_email1"),
            "password": os.getenv("user_password")
        }
        response = session.get(f"{self.browser.kk_url}/auth/realms/master/account/")
        auth_url = re.search(r"auth.*authenticate\?session_code.*(?=\"\s)", response.text)[0].replace('&amp;', '&')
        session.post(f"{self.browser.kk_url}/{auth_url}", payload)
        self.browser.get(f"{self.browser.kk_url}/auth/realms/master/account/")
        for key, value in session.cookies.get_dict().items():
            self.browser.add_cookie({"name": f'{key}', "value": f'{value}', "Domain": "id-preprod.etpgpb.ru",
                                     "Path": "/auth/realms/master", "expiry": 1680537903})
        self.browser.refresh()
        self.browser.get(self.browser.url)
        return self.browser

    def get_auth_user_cookie(self):
        session = requests.Session()
        payload = {
            "username": os.getenv("user_email1"),
            "password": os.getenv("user_password")
        }
        response = session.get(f"{self.browser.kk_url}/auth/realms/master/account/")
        auth_url = re.search(r"auth.*authenticate\?session_code.*(?=\"\s)", response.text)[0].replace('&amp;', '&')
        session.post(f"{self.browser.kk_url}/{auth_url}", payload)
        self.browser.get(f"{self.browser.kk_url}/auth/realms/master/account/")
        for key, value in session.cookies.get_dict().items():
            self.browser.add_cookie({"name": f'{key}', "value": f'{value}', "Domain": "id-preprod.etpgpb.ru",
                                     "Path": "/auth/realms/master", "expiry": 1680537903})
        self.browser.refresh()
        self.browser.get(self.browser.url)
        return self.browser
