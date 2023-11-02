from pages.tensor_about_page import TensorAboutPage


class TestTensorAboutPage:
    def test_guest_can_find_work_images(self, driver):
        page = TensorAboutPage(driver, "https://tensor.ru/about")
        page.open()
        page.find_work_images()

    def test_work_images_are_equal_in_size(self, driver):
        page = TensorAboutPage(driver, "https://tensor.ru/about")
        page.open()
        images = page.find_work_images()
        image_sizes = {
            (img.size["width"], img.size["height"]) for img in images
        }
        assert len(image_sizes) == 1
