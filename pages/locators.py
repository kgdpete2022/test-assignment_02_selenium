from selenium.webdriver.common.by import By


class Locators:
    CONTACTS_LINK = (By.XPATH, "//ul/li/a[text()='Контакты']")
    TENSOR_LINK = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    # STRENGTH_IN_PEOPLE_BLOCK = (
    #     By.XPATH,
    #     "//div//p[contains(text(), 'Сила в людях')]/ ..",
    # )
    DETAILS_LINK = (
        By.XPATH,
        "//div//p[contains(text(), 'Сила в людях')]/ ../p/a",
    )
    WORK_IMAGES = (
        By.XPATH,
        "//h2[contains(text(),'Работаем')]/ ../..//div[2]//img",
    )

