import pytest

from Configurations.ReadConfig import ReadConfig
from Logs import Logger
from PageObjects.LoginPage import LoginPage
from TestData.DataProvider import DataProvider


class TestDepartment:
    url = ReadConfig.get_application_url()
    login_email = ReadConfig.get_valid_login_email()
    login_password = ReadConfig.get_valid_login_password()

    logger = Logger.Logger.get_logger()

    def test_department(self, setup, get_data):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestAddDepartment")

        login_page = LoginPage(self.driver)

        homepage = login_page.do_login(self.login_email, self.login_password)
        if homepage is not None:
            self.logger.info('Logged In Successfully')
            result = homepage.navigate_to_employees_app()
            if result is not None:
                self.logger.info('navigated to employees app')

                dept_page = homepage.navigate_to_app_department()

                emp_page = dept_page.add_a_department(get_data['dept_name'],
                                                      get_data['parent_dept_name'],
                                                      get_data['manager_name'],
                                                      get_data['sheet_name'],
                                                      get_data['rowNum'])
                if emp_page is not None:
                    self.logger.info('one dept added successfully')

                logout = homepage.do_logout()
                if logout is not None:
                    self.logger.info('successfully logged out')
        else:
            self.logger.error('Login failed')

        self.driver.quit()

    @pytest.fixture(params=DataProvider.get_test_data('Test_data_for_department'))
    def get_data(self, request):
        return request.param
