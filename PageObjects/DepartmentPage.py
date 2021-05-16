from selenium.webdriver.common.by import By

from Configurations.ReadConfig import ReadConfig
from PageObjects.BasePage import BasePage
from PageObjects.EmoloyeePage import EmployeePage
from utilities import ScreenShot, ExcelUtil


class DepartmentPage(BasePage):
    CREATE = (By.XPATH, "//button[text()[normalize-space()='Create']]")
    dep_name = (By.NAME, "name")

    parent_department_dropdown = (By.XPATH, "(//label[text()='Parent Department']/following::input)[1]")
    all_parent_department = '//td[@class="o_data_cell o_readonly_modifier"]'

    manager_dropdown = (By.XPATH, "(//label[text()='Manager']/following::input)[1]")
    search_more = (By.LINK_TEXT, "Search More...")
    all_managers = '//td[@class="o_data_cell"][1]'

    SAVE = (By.XPATH, "//button[text()[normalize-space()='Save']]")
    EDIT = (By.XPATH, "//button[text()[normalize-space()='Edit']]")

    def __init__(self, driver):
        super().__init__(driver)

    def add_a_department(self, dept_name, parent_dept_name, manager_name, sheet_name, rownum):
        try:
            self.click(self.CREATE)
            self.wait_till_click(self.SAVE)
            self.clearAndType(self.dep_name, dept_name)
            self.click(self.parent_department_dropdown)
            self.click(self.search_more)
            self.select_from_table(self.all_parent_department, parent_dept_name)
            self.click(self.manager_dropdown)
            self.click(self.search_more)
            self.select_from_table(self.all_managers, manager_name)
            self.click(self.SAVE)
            self.wait_till_click(self.EDIT)
            assert parent_dept_name+" / "+dept_name+" - Odoo" == self.driver.title
            ScreenShot.take_screenshot(self.driver, 'department: ' + dept_name + ' Details')
            if rownum != 0:
                ExcelUtil.write_data(ReadConfig.ReadConfig.get_test_report_excel_path(),
                                     sheet_name, rownum, 6,
                                     "department added successfully ")
                ExcelUtil.write_data(ReadConfig.ReadConfig.get_test_report_excel_path(),
                                     sheet_name, rownum, 7,
                                     'Pass')

            return EmployeePage(self.driver)

        except Exception:
            ScreenShot.take_screenshot(self.driver, 'Error while creating Department ' + dept_name)
            if rownum != 0:
                ExcelUtil.write_data(ReadConfig.ReadConfig.get_test_report_excel_path(),
                                     sheet_name, rownum, 6,
                                     "Error while adding department")
                ExcelUtil.write_data(ReadConfig.ReadConfig.get_test_report_excel_path(),
                                     sheet_name, rownum, 7,
                                     'Pass')

            return None
