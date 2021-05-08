import pytest

from Logs.Logger import Logger
from PageObjects.LoginPage import LoginPage
from TestData import DataProvider
from utilities import ReadConfig


class TestLogin:

    logger = Logger.get_logger()
    i = 0

    def test_login(self, setup, get_data):
        self.driver = setup
        self.driver.get(ReadConfig.ReadConfig.get_application_url())
        self.driver.maximize_window()

        self.logger.info("Test_Login_"+str(self.i)+"")
        self.i += 1

        login_page = LoginPage(self.driver)

        homepage = login_page.do_login(get_data['username'],
                                       get_data['password'])
        if homepage is not None:
            self.logger.info('Logged In Successfully')

            result = homepage.do_logout()
            if result is not None:
                self.logger.info('logged out successfully')
            else:
                self.logger.error('logout failed')

        else:
            self.logger.error('Login failed')

        self.driver.quit()

    @pytest.fixture(params=DataProvider.DataProvider.get_test_data('Test_data_for_login'))
    def get_data(self, request):
        return request.param