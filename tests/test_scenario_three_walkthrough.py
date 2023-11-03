import time

from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_main_page import SbisMainPage


class TestScenarioThree:
    def test_scenario_two_walkthrough(self, driver):
        page = SbisMainPage(driver, "https://sbis.ru")
        page.open()
        assert driver.current_url == "https://sbis.ru/"
        page.go_to_download_page()
        assert (
            driver.current_url
            == "https://sbis.ru/download?tab=ereport&innerTab=ereport25"
        )
        time.sleep(2)
        page = SbisDownloadPage(driver, driver.current_url)
        page.go_to_sbis_plugin_tab()
        page.download_sbis_plugin()
        time.sleep(2)
