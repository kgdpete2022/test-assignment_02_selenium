import os

from selenium.webdriver.common.by import By

from .base_page import BasePage


class SbisDownloadPageLocators:
    LOCATOR_SBIS_PLUGIN_TAB = (
        By.XPATH,
        "//div[@class='controls-TabButton__caption'][contains(text(), 'СБИС Плагин')]",
    )
    LOCATOR_SBIS_PLUGIN_DOWNLOAD_LINK = (
        By.XPATH,
        "//h3[contains(text(), 'Веб-установщик')]/ ../..//a",
    )


class SbisDownloadPage(BasePage):
    def go_to_sbis_plugin_tab(self):
        sbis_plugin_tab_link = self.element_is_visible(
            SbisDownloadPageLocators.LOCATOR_SBIS_PLUGIN_TAB
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", sbis_plugin_tab_link
        )
        self.driver.execute_script(
            "arguments[0].click();", sbis_plugin_tab_link
        )

    def find_sbis_plugin_download_link(self):
        return self.element_is_visible(
            SbisDownloadPageLocators.LOCATOR_SBIS_PLUGIN_DOWNLOAD_LINK
        )

    def get_sbis_plugin_file_size(self):
        link_text = self.find_sbis_plugin_download_link().text
        return link_text.split()[-2]

    def download_sbis_plugin(self):
        self.find_sbis_plugin_download_link().click()
        # alert = self.driver.switch_to_alert()
        # alert.accept()

    def get_size_of_downloaded_file(self):
        pass
