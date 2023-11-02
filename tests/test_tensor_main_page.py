from pages.tensor_main_page import TensorMainPage


class TestTensorMainPage:
    def test_guest_can_find_strength_in_the_people_block(self, driver):
        page = TensorMainPage(driver, "https://tensor.ru")
        page.open()
        page.find_strength_in_the_people_block()

    def test_guest_can_follow_strength_in_the_people_block_details_link(
        self, driver
    ):
        page = TensorMainPage(driver, "https://tensor.ru")
        page.open()
        page.follow_strength_in_the_people_block_details_link()

    def test_details_link_leads_to_tensor_about_page(self, driver):
        page = TensorMainPage(driver, "https://tensor.ru")
        page.open()
        page.follow_strength_in_the_people_block_details_link()
        assert driver.current_url == "https://tensor.ru/about"
