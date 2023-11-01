# 1) Перейти на https://sbis.ru/ в раздел "Контакты"
# 2) Найти баннер Тензор, кликнуть по нему
# 3) Перейти на https://tensor.ru/
# 4) Проверить, что есть блок "Сила в людях"
# 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
# https://tensor.ru/about
# 6) Находим раздел Работаем и проверяем, что у всех фотографии
# хронологии одинаковые высота (height) и ширина (width)
from selenium import webdriver

from pages.base_page import BasePage
from pages.locators import Locators

# 1) Перейти на https://sbis.ru/ в раздел "Контакты"


def test_should_see_contacts_link():
    driver = webdriver.Chrome()
    link = "https://sbis.ru/"
    page = BasePage(driver, link)
    page.open()
    assert page.is_element_present(
        *Locators.CONTACTS_LINK
    ), "Contacts link is not present"


def test_should_see_mainpage_url():
    driver = webdriver.Chrome()
    link = "https://sbis.ru/"
    page = BasePage(driver, link)
    page.open()
    assert page.is_url_correct(link), "The url is not https://sbis.ru/"
