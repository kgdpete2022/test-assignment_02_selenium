from .base_page import BasePage
from .locators import Locators


class MainPage(BasePage):
    def should_see_contacts_link(self):
        assert self.is_element_present(
            *Locators.CONTACTS_LINK
        ), "Contacts link is not present"

    def should_see_mainpage_url(self):
        assert (
            self.browser.current_url == "https://sbis.ru/"
        ), "Main page url is not https://sbis.ru/"
