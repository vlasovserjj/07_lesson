from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)

    def click_chek(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()