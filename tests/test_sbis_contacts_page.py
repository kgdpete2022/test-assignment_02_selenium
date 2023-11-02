from pages.sbis_contacts_page import SbisContactsPage


class TestSbisContactsPage:
    def test_guest_can_find_tensor_banner(self, driver):
        page = SbisContactsPage(driver, "https://sbis.ru/contacts")
        page.open()
        page.find_tensor_banner()

    def test_guest_can_go_to_tensor_main_page(self, driver):
        page = SbisContactsPage(driver, "https://sbis.ru/contacts")
        page.open()
        page.go_to_tensor_main_page()
