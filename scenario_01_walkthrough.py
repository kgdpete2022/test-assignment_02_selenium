# 1) Перейти на https://sbis.ru/ в раздел "Контакты"
# 2) Найти баннер Тензор, кликнуть по нему
# 3) Перейти на https://tensor.ru/
# 4) Проверить, что есть блок "Сила в людях"
# 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
# https://tensor.ru/about
# 6) Находим раздел Работаем и проверяем, что у всех фотографии
# хронологии одинаковые высота (height) и ширина (width)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import Locators
from utils import are_equal_in_size

if __name__ == "__main__":
    try:
        # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
        driver = webdriver.Chrome()
        link = "https://sbis.ru/"
        sb_main_page = BasePage(driver, link)
        sb_main_page.open()
        time.sleep(1)

        contacts_page_link = sb_main_page.select_element(
            *Locators.CONTACTS_LINK
        )
        time.sleep(1)
        contacts_page_link.click()

        # 2) Найти баннер Тензор, кликнуть по нему
        # 3) Перейти на https://tensor.ru/

        tensor_banner_link = driver.find_element(*Locators.TENSOR_LINK)
        tensor_banner_link.click()

        cur_window = driver.current_window_handle

        for w in driver.window_handles:
            if w != cur_window:
                driver.switch_to.window(w)
                break

        # 4) Проверить, что есть блок "Сила в людях"
        # 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
        # https://tensor.ru/about
        tensor_main_page = BasePage(driver, driver.current_url)
        tensor_main_page.open()

        details_link = tensor_main_page.select_element(
            *Locators.DETAILS_LINK,
        )

        driver.execute_script(
            "arguments[0].scrollIntoView(true);", details_link
        )
        driver.execute_script("arguments[0].click();", details_link)
        time.sleep(5)

        # 6) Находим раздел Работаем и проверяем, что у всех фотографии
        # хронологии одинаковые высота (height) и ширина (width)
        tensor_about_page = BasePage(driver, driver.current_url)
        work_images = tensor_about_page.select_elements(*Locators.WORK_IMAGES)

        for img in work_images:
            print(img.size["width"], img.size["height"])

    finally:
        driver.quit()
