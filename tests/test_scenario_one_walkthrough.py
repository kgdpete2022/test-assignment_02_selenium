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
        page.find_tensor_banner().click()
        page = TensorMainPage(driver, "")
