import calendar
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from utilities import CustomWait


class BasePage:

    daycen = (By.XPATH, "(//div[@class='datepicker-days'])/table/thead/tr/th[@class='picker-switch']")
    monthcen = (By.XPATH, "(//div[@class='datepicker-months'])/table/thead/tr/th[@class='picker-switch']")
    yearcen = (By.XPATH, '(//div[@class="datepicker-years"])/table/thead/tr/th[@class="picker-switch"]')

    yearprev = (By.XPATH, '(//div[@class="datepicker-years"])/table/thead/tr/th[@class="prev"]')
    yearnext = (By.XPATH, '(//div[@class="datepicker-years"])/table/thead/tr/th[@class="next"]')

    getalldays = '//table[@class="table table-sm"]/tbody/tr/td[@class="day active" or @class="day" or @class="day weekend" or @class="day today"]'
    getallmonth = '(//div[@class="datepicker-months"])/table/tbody/tr/td/span'
    getallyears = '(//div[@class="datepicker-years"])/table/tbody/tr/td/span'

    def __init__(self, driver):
        self.driver = driver

    def wait_till_click(self, by_locator):
        CustomWait.wait(self.driver, 'click', by_locator)

    def wait_till_presence(self, by_locator):
        CustomWait.wait(self.driver, 'presence', by_locator)

    def get_element(self, xpath):
        ele = self.driver.find_element_by_xpath(xpath)
        return ele

    def click(self, by_locator):
        CustomWait.wait(self.driver, 'click', by_locator).click()

    def click_and_enter(self, by_locator):
        ele = CustomWait.wait(self.driver, 'click', by_locator)
        ele.click()
        time.sleep(120)
        ele.send_keys(Keys.RETURN)

    def clearAndType(self, by_locator, value):
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        ele.clear()
        ele.send_keys(value)

    def getText(self, by_locator):
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        return ele.text

    def get_all_elements(self, xpath):
        result = self.driver.find_elements_by_xpath(xpath)
        return result

    def select_from_dropdown(self, by_locator, text):
        ele = Select(CustomWait.wait(self.driver, 'presence', by_locator))
        ele.select_by_visible_text(text)

    def select_date(self, date_string):

        day = int(date_string.strftime("%d"))
        month = int(date_string.strftime("%m"))
        year = int(date_string.strftime("%Y"))
        self.click(self.daycen)
        self.click(self.monthcen)

        while True:
            year_range = self.getText(self.yearcen)
            year_range_list = year_range.split('-')
            if int(year_range_list[0]) <= year <= int(year_range_list[1]):
                all_years = self.get_all_elements(self.getallyears)
                for yrs in all_years:
                    if int(yrs.text) == year:
                        yrs.click()
                        break
                all_months = self.get_all_elements(self.getallmonth)
                for mon in all_months:
                    if mon.text == calendar.month_abbr[month]:
                        mon.click()
                        break
                all_days = self.get_all_elements(self.getalldays)
                for da in all_days:
                    if int(da.text) == day:
                        da.click()
                        break
                break
            elif year < int(year_range_list[0]):
                self.click(self.yearprev)
            elif year > int(year_range_list[1]):
                self.click(self.yearnext)

    def select_from_table(self, xpath, txt):
        time.sleep(5)
        all_customer = self.get_all_elements(xpath)
        for x in all_customer:
            if x.text == txt:
                actions = ActionChains(self.driver)
                actions.move_to_element(x)
                actions.perform()
                x.click()
                break
        time.sleep(5)

    def is_element_exist(self, by_locator):
        try:
            element = CustomWait.wait(self.driver, 'presence', by_locator)
        except TimeoutException:
            element = False
        return True if element else False


