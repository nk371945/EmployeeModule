import pytest

from Logs.Logger import Logger
from PageObjects.LoginPage import LoginPage
from utilities import ReadConfig


class TestAddEmployee:

    url = ReadConfig.ReadConfig.get_application_url()
    login_email = ReadConfig.ReadConfig.get_valid_login_email()
    login_password = ReadConfig.ReadConfig.get_valid_login_password()

    logger = Logger.get_logger()

    def test_employee(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestAddEmployee")

        login_page = LoginPage(self.driver)

        homepage = login_page.do_login(self.login_email, self.login_password)
        if homepage is not None:
            self.logger.info('Logged In Successfully')
        else:
            self.logger.error('Login failed')

        result = homepage.do_logout()
        if result is not None:
            self.logger.info('logged out successfully')
        else:
            self.logger.error('logout failed')
        self.driver.quit()

