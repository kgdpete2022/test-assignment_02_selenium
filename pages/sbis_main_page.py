from selenium.webdriver.common.by import By

from .base_page import BasePage
from .sbis_contacts_page import SbisContactsPage


class SbisMainPageLocators:
    LOCATOR_CONTACTS_LINK = (By.XPATH, "//ul/li/a[text()='Контакты']")


class SbisMainPage(BasePage):
    def find_contacts_link(self):
        return self.element_is_visible(
            SbisMainPageLocators.LOCATOR_CONTACTS_LINK
        )

    def go_to_sbis_contacts_page(self):
        self.find_contacts_link().click()
