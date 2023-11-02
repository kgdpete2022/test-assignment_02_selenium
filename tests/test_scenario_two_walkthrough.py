import time

from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_main_page import SbisMainPage


class TestScenarioTwo:
    def test_scenario_two_walkthrough(self, driver):
        page = SbisMainPage(driver, "https://sbis.ru")
        page.open()
        page.go_to_sbis_contacts_page()
        time.sleep(2)
        page = SbisContactsPage(driver, driver.current_url)
        region_before_change = page.find_identified_region().text
        partners_before_change = page.find_partners()
        page.change_region()
        time.sleep(2)
        region_after_change = page.find_identified_region().text
        partners_after_change = page.find_partners()

        assert "kamchatskij-kraj" in page.driver.current_url
        assert "Камчатский край" in page.driver.title
        assert region_before_change != region_after_change
        assert partners_before_change != partners_after_change
        time.sleep(2)
