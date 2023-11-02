from selenium.webdriver.common.by import By

from .base_page import BasePage


class TensorAboutPageLocators:
    LOCATOR_WORK_IMAGES = (
        By.XPATH,
        "//h2[contains(text(),'Работаем')]/ ../..//div[2]//img",
    )


class TensorAboutPage(BasePage):
    def find_work_images(self):
        return self.elements_are_visible(
            TensorAboutPageLocators.LOCATOR_WORK_IMAGES
        )

    def work_images_dimensions_are_equal(self):
        images = self.find_work_images()
        dimensions = {
            (img.size["width"], img.size["height"]) for img in images
        }
        return len(dimensions) == 1
