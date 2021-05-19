from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.DepartmentPage import DepartmentPage
from PageObjects.EmoloyeePage import EmployeePage
from Configurations import ReadConfig


class HomePage(BasePage):
    user_menu = (By.XPATH, "(//li[@class='o_user_menu']//a)[1]")
    app_list = (By.CLASS_NAME, "full")

    module_name_link_text = (By.LINK_TEXT, "{module_name}")
    name = ReadConfig.ReadConfig.get_module_name()
    employee_txt = (By.XPATH, "//li[text()='Employees']")

    department_menu = (By.LINK_TEXT, "Departments")
    departments_txt = (By.XPATH, "// li[text() = 'Departments']")

    employee_menu = (By.LINK_TEXT, "Employees")

    logout_btn = (By.XPATH, "//a[@data-menu='logout']")
    OK = "//span[text()='Ok']"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_module(self):
        self.click(self.app_list)
        mod = list(self.module_name_link_text)
        mod[1] = mod[1].format(module_name=self.name)
        self.click(tuple(mod))
        self.wait_till_presence(self.employee_txt)
        return EmployeePage(self.driver)

    def navigate_to_add_employee(self):
        self.click(self.employee_menu)
        self.wait_till_presence(self.employee_txt)
        return EmployeePage(self.driver)

    def navigate_to_app_department(self):
        self.click(self.department_menu)
        self.wait_till_presence(self.departments_txt)
        return DepartmentPage(self.driver)

    def do_logout(self):
        self.click(self.user_menu)
        self.click(self.logout_btn)
        try:
            if self.get_element(self.OK).is_displayed():
                self.get_element(self.OK).click()
        except Exception:
            pass
        if "Odoo" == self.driver.title:
            return "Done"
        else:
            return None

