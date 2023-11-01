from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def select_element(self, locator, value):
        return self.driver.find_element(locator, value)

    def select_elements(self, locator, value):
        return self.driver.find_elements(locator, value)

    def is_element_present(self, locator, value):
        try:
            self.select_element(locator, value)
        except NoSuchElementException:
            return False
        return True

    def is_url_correct(self, url):
        return self.driver.current_url == url
