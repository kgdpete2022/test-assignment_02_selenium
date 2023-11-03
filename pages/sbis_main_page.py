from selenium.webdriver.common.by import By

from .base_page import BasePage
from .sbis_contacts_page import SbisContactsPage


class SbisMainPageLocators:
    LOCATOR_CONTACTS_LINK = (By.XPATH, "//ul/li/a[text()='Контакты']")
    LOCATOR_SBIS_DOWNLOAD_PAGE_LINK = (
        By.XPATH,
        "//a[@class='sbisru-Footer__link'][contains(text(), 'Скачать СБИС')]",
    )


class SbisMainPage(BasePage):
    def find_contacts_link(self):
        return self.element_is_visible(
            SbisMainPageLocators.LOCATOR_CONTACTS_LINK
        )

    def go_to_sbis_contacts_page(self):
        self.find_contacts_link().click()

    def find_sbis_download_page_link(self):
        return self.element_is_visible(
            SbisMainPageLocators.LOCATOR_SBIS_DOWNLOAD_PAGE_LINK
        )

    def go_to_download_page(self):
        download_page_link = self.find_sbis_download_page_link()

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", download_page_link
        )
        self.driver.execute_script("arguments[0].click();", download_page_link)
