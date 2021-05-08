import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

"""
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # print('*****', outcome, '*****')
    # print('*****', rep.nodeid, '*****')
    # print('*****', rep.location, '*****')
    # print('*****', item, '*****')
    # print('*****', call, '*****')

    #if rep.outcome == 'failed':
        #allure.attach(driver.get_screenshot_as_png(), name=rep.nodeid, attachment_type=AttachmentType.PNG)
    # setattr(item, "rep_" + rep.when, rep)
    # return rep
"""