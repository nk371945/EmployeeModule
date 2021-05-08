import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from utilities import ScreenShot, ExcelUtil, ReadConfig


class EmployeePage(BasePage):
    create = (By.XPATH, "//button[text()[normalize-space()='Create']]")

    emp_name = (By.NAME, "name")

    emp_type = (By.XPATH, "(//label[text()='Name']/following::input)[2]")
    all_emp_type = '//ul[@class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content"]/li'

    work_address_dropdown = (By.XPATH, "(//label[text()='Work Address']/following::input)[1]")
    search_more = (By.LINK_TEXT, "Search More...")
    all_work_address = '//td[@class="o_data_cell o_readonly_modifier"]'

    work_location = (By.NAME, "work_location")
    work_email = (By.NAME, "work_email")
    work_mobile = (By.NAME, "mobile_phone")

    dept_dropdown = (By.XPATH, "(//label[text()='Department']/following::input)[1]")
    all_dept = '//li[@class="ui-menu-item"]'

    job_position_dropdown = (By.XPATH, "(//label[text()='Job Position']/following::input)[1]")
    all_job_positions = '//li[@class="ui-menu-item"]'

    manager_dropdown = (By.XPATH, "(//label[text()='Manager']/following::input)[1]")
    all_managers = '//td[@class="o_data_cell"][1]'

    save = (By.XPATH, "//button[text()[normalize-space()='Save']]")
    edit = (By.XPATH, "//button[text()[normalize-space()='Edit']]")

    all_emp = '//strong[@class="o_kanban_record_title"]/span'

    payslip_btn = (By.XPATH, "(//button[@class='btn oe_stat_button'])[3]")

    emp_name_in_table = (By.  XPATH, "//tr[@class='o_group_header o_group_has_content']")
    payslip_name = (By.XPATH, '//tr[@class="o_data_row"]/td[4]')
    name = (By.NAME, "name")
    print_btn = (By.XPATH, "//button[text()[normalize-space()='Print']]")
    payslip = (By.LINK_TEXT, "Payslip")

    action_btn = (By.XPATH, "//button[text()[normalize-space()='Action']]")
    delete_btn = (By.XPATH, "//a[text()[normalize-space()='Delete']]")
    OK = "//span[text()='Ok']"

    def __init__(self, driver):
        super().__init__(driver)

    def add_a_employee(self, employee_name, employee_type, work_address, work_loc, email, mobile, dept, job_position, manager, sheet_name, rownum):
        try:
            self.click(self.create)
            self.wait_till_click(self.save)

            self.clearAndType(self.emp_name, employee_name)
            self.click(self.emp_type)
            self.select_from_table(self.all_emp_type, employee_type)
            self.click(self.work_address_dropdown)
            time.sleep(5)
            self.click(self.search_more)
            self.select_from_table(self.all_work_address, work_address)
            time.sleep(5)
            self.clearAndType(self.work_location, work_loc)
            self.clearAndType(self.work_email, email)
            self.clearAndType(self.work_mobile, mobile)
            self.click(self.dept_dropdown)
            self.select_from_table(self.all_dept, dept)
            self.click(self.job_position_dropdown)
            self.select_from_table(self.all_job_positions, job_position)
            self.click(self.manager_dropdown)
            self.click(self.search_more)
            self.select_from_table(self.all_managers, manager)

            self.click(self.save)
            self.wait_till_click(self.edit)

            assert employee_name+" - Odoo" == self.driver.title
            ScreenShot.takeScreenshot(self.driver, 'Employee ' + employee_name + ' Details')
            if rownum != 0:
                ExcelUtil.write_data(ReadConfig.getValues('test_report_file'),
                                     sheet_name, rownum, 6,
                                     "employee added successfully ")
                ExcelUtil.write_data(ReadConfig.getValues('test_report_file'),
                                     sheet_name, rownum, 7,
                                     'Pass')
            return "Pass"

        except Exception:
            ScreenShot.takeScreenshot(self.driver, 'Error while adding new employee ' + employee_name)
            if rownum != 0:
                ExcelUtil.write_data(ReadConfig.getValues('test_report_file'),
                                     sheet_name, rownum, 6,
                                     "Error while adding employee")
                ExcelUtil.write_data(ReadConfig.getValues('test_report_file'),
                                     sheet_name, rownum, 7,
                                     'Pass')
            return None

    def delete_employee(self, empName):
        time.sleep(5)
        self.select_from_table(self.all_emp, empName)
        self.click(self.action_btn)
        self.click(self.delete_btn)
        time.sleep(5)
        try:
            if self.get_element(self.OK).is_displayed():
                ScreenShot.takeScreenshot(self.driver, 'deletion of Employee')
                self.get_element(self.OK).click()
                time.sleep(10)
        except NoSuchElementException:
            pass
        return "success"





