import pytest

from Logs.Logger import Logger
from PageObjects.LoginPage import LoginPage
from Configurations import ReadConfig
from TestData import DataProvider


class TestAddEmployee:
    url = ReadConfig.ReadConfig.get_application_url()
    login_email = ReadConfig.ReadConfig.get_valid_login_email()
    login_password = ReadConfig.ReadConfig.get_valid_login_password()

    logger = Logger.get_logger()

    def test_add_employee(self, setup, get_data):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestAddEmployee")

        login_page = LoginPage(self.driver)

        homepage = login_page.do_login(self.login_email, self.login_password)
        if homepage is not None:
            self.logger.info('Logged In Successfully')

            navi_emp_app = homepage.navigate_to_employees_app()
            if navi_emp_app is not None:
                self.logger.info('navigated to employee module')
            else:
                self.logger.error('error while navigating to employee module')

            emp_page = homepage.navigate_to_add_employee()
            if emp_page is not None:
                self.logger.info('navigated to add employee form')
            else:
                self.logger.error('error while navigating to add employee form')

            add_emp = emp_page.add_a_employee(get_data['employee_name'],
                                              get_data['employee_type'],
                                              get_data['work_address'],
                                              get_data['work_loc'],
                                              get_data['email'],
                                              get_data['mobile'],
                                              get_data['dept'],
                                              get_data['job_position'],
                                              get_data['manager'],
                                              get_data['sheet_name'],
                                              get_data['rowNum'])

            if add_emp is not None:
                self.logger.info('One employee added successfully')
            else:
                self.logger.error('error while adding employee')

            result = homepage.do_logout()
            if result is not None:
                self.logger.info('logged out successfully')
            else:
                self.logger.error('logout failed')
        else:
            self.logger.error('Login failed')

        self.driver.quit()

    @pytest.fixture(params=DataProvider.DataProvider.get_test_data('Test_data_for_employee'))
    def get_data(self, request):
        return request.param
