import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": f"{os.getcwd()}\\tests\\",
        "safebrowsing.enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
