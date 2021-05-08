from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.EmoloyeePage import EmployeePage


class HomePage(BasePage):
    user_menu = (By.XPATH, "(//li[@class='o_user_menu']//a)[1]")
    app_list = (By.CLASS_NAME, "full")

    employee_app = (By.LINK_TEXT, "Employees")
    employee_txt = (By.XPATH, "//li[text()='Employees']")

    employee_menu = (By.LINK_TEXT, "Employees")

    logout_btn = (By.XPATH, "//a[@data-menu='logout']")
    OK = "//span[text()='Ok']"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_employees_app(self):
        self.click(self.app_list)
        self.click(self.employee_app)
        self.wait_till_presence(self.employee_txt)
        return EmployeePage(self.driver)

    def navigate_to_add_employee(self):
        self.click(self.employee_menu)
        self.wait_till_presence(self.employee_txt)
        return EmployeePage(self.driver)

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

