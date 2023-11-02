from selenium.webdriver.common.by import By

from .base_page import BasePage
from .tensor_about_page import TensorAboutPage


class TensorMainPageLocators:
    LOCATOR_PEOPLE_BLOCK = (
        By.XPATH,
        "//div//p[contains(text(), 'Сила в людях')]",
    )
    LOCATOR_PEOPLE_BLOCK_DETAILS_LINK = (
        By.XPATH,
        "//div//p[contains(text(), 'Сила в людях')]/ ../p/a",
    )


class TensorMainPage(BasePage):
    def find_strength_in_the_people_block(self):
        self.element_is_visible(TensorMainPageLocators.LOCATOR_PEOPLE_BLOCK)

    def follow_strength_in_the_people_block_details_link(self):
        details_link = self.element_is_visible(
            TensorMainPageLocators.LOCATOR_PEOPLE_BLOCK_DETAILS_LINK
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", details_link
        )
        self.driver.execute_script("arguments[0].click();", details_link)
