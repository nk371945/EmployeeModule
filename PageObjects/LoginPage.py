import time

from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage
from selenium.webdriver.common.by import By
from utilities import ReadConfig, ExcelUtil, ScreenShot


class LoginPage:
    user_name_xpath = (By.XPATH, "//input[@placeholder='Email']")
    password_xpath = (By.XPATH, "//input[@placeholder='Password']")
    login_btn_xpath = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")
    alert_xpath = (By.XPATH, "//p[@class='alert alert-danger']")
    text = (By.XPATH, "//div[text()='New messages appear here.']")

    def __init__(self, driver):
        self.driver = driver

    def do_login(self, username, password):
        base = BasePage(self.driver)

        base.clearAndType(self.user_name_xpath, username)
        base.clearAndType(self.password_xpath, password)
        ScreenShot.take_screenshot(self.driver, 'credentials_filled')
        base.click(self.login_btn_xpath)

        try:
            base.wait_till_click(self.alert_xpath)

        except Exception:
            base.wait_till_presence(self.text)
            print(self.driver.title)
            if "Inbox - Odoo" == self.driver.title:
                ScreenShot.take_screenshot(self.driver, 'successfully_logged_in')
                return HomePage(self.driver)

        value = base.getText(self.alert_xpath)
        ScreenShot.take_screenshot(self.driver, value)

        return None



