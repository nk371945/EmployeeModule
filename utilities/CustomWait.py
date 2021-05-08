from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(driver, waitType, by_locator):
    w = WebDriverWait(driver, 30)
    ele = None

    if waitType == 'click':
        ele = w.until(EC.element_to_be_clickable(by_locator))
    elif waitType == 'presence':
        ele = w.until(EC.presence_of_element_located(by_locator))

    return ele
