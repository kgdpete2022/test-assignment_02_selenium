from selenium.webdriver.common.by import By

from .base_page import BasePage


class SbisContactsPageLocators:
    LOCATOR_TENSOR_BANNER = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")

    LOCATOR_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")

    LOCATOR_REGIONS_TABLE = (
        By.XPATH,
        "//div[@class='sbis_ru-Region-Panel__container']/ ..",
    )

    LOCATOR_PARTNERS = (By.CLASS_NAME, "sbisru-Contacts-List__name")

    LOCATOR_KAMCHATKA = (
        By.XPATH,
        "//span[@class='sbis_ru-link'][contains(text(), 'Камчатский край')]",
    )


class SbisContactsPage(BasePage):
    def find_tensor_banner(self):
        return self.element_is_visible(
            SbisContactsPageLocators.LOCATOR_TENSOR_BANNER
        )

    def go_to_tensor_main_page_using_banner(self):
        tensor_banner = self.find_tensor_banner()
        tensor_banner.click()

        cur_window = self.driver.current_window_handle

        for w in self.driver.window_handles:
            if w != cur_window:
                self.driver.switch_to.window(w)
                break

    def find_identified_region(self):
        return self.element_is_visible(SbisContactsPageLocators.LOCATOR_REGION)

    def find_partners(self):
        partners_temp = self.elements_are_visible(
            SbisContactsPageLocators.LOCATOR_PARTNERS
        )
        partners = [partner.text for partner in partners_temp]
        return sorted(partners)

    def invoke_regions_table(self):
        self.find_identified_region().click()

    def change_region(self):
        self.invoke_regions_table()
        self.element_is_visible(
            SbisContactsPageLocators.LOCATOR_KAMCHATKA
        ).click()
