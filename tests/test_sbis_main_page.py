from pages.sbis_main_page import SbisMainPage


class TestSbisMainPage:
    def test_guest_can_go_to_sbis_contacts_page(self, driver):
        page = SbisMainPage(driver, "https://sbis.ru")
        page.open()
        page.go_to_sbis_contacts_page()
