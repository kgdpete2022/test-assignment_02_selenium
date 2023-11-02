import time

from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_main_page import SbisMainPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_main_page import TensorMainPage


class TestScenarioOne:
    def test_scenario_one_walkthrough(self, driver):
        page = SbisMainPage(driver, "https://sbis.ru")
        page.open()
        page.go_to_sbis_contacts_page()
        time.sleep(2)
        page = SbisContactsPage(driver, driver.current_url)
        page.go_to_tensor_main_page_using_banner()
        time.sleep(2)
        page = TensorMainPage(driver, driver.current_url)
        assert page.find_strength_in_the_people_block()
        page.follow_strength_in_the_people_block_details_link()
        assert driver.current_url == "https://tensor.ru/about"
        page = TensorAboutPage(driver, driver.current_url)
        assert page.work_images_dimensions_are_equal()
